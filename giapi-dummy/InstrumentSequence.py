#!/usr/bin/env python3

import cppyy
import os, time, sys
from threading import Thread
from HKPcc import HKPcc
giapi_root=os.environ.get("GIAPI_ROOT")
cppyy.add_include_path(f"{giapi_root}/install/include")
cppyy.add_library_path(f"{giapi_root}/install/lib")
cppyy.include("giapi/StatusUtil.h")
cppyy.include("giapi/SequenceCommandHandler.h")
cppyy.include("giapi/CommandUtil.h")
cppyy.include("giapi/HandlerResponse.h")
cppyy.include("giapi/DataUtil.h")
cppyy.load_library("libgiapi-glue-cc")
cppyy.add_include_path(f"{giapi_root}/src/examples/InstrumentDummyPython")
cppyy.include("DataResponse.h")
cppyy.include("InstCmdHandler.h")
from cppyy.gbl import giapi
from cppyy.gbl import instDummy
sys.path.append("../")
from Libs.MsgMiddleware import MsgMiddleware
from HK_def import *


class InstrumentSequencer:
    
    def __init__(self):
        self._ipAddr = 'localhost'
        self._id = 'InstSeq-id'
        self._callbackGiapi = self.callbackGiapi
        self._exchangeHKP = 'HKPtoCli' 
        self._routingHKP = ['ALARM', 'WARM']
        self._hkp = MsgMiddleware(self._ipAddr, self._exchangeHKP, 'direct')
        
        self._routingDetector = ['COMPLETED', 'INFO','ALARM','WARM']
        self._routingDetPro = ['CMD']
        self._exchangeDTkCl = 'DTKToCli' 
        self._dtkCl= MsgMiddleware(self._ipAddr, self._exchangeDTkCl, 'direct')
        self._exchangeDTkPro = 'CliToDTK' 
        self._dtkProd= MsgMiddleware(self._ipAddr, self._exchangeDTkPro, 'direct', False)
        
        
        self._exchangeDThCl = 'DTHToCli' 
        self._dthCl = MsgMiddleware(self._ipAddr, self._exchangeDThCl, 'direct')
        self._exchangeDThPro = 'CliToDTH' 
        self._dthProd= MsgMiddleware(self._ipAddr, self._exchangeDThPro, 'direct', False)
        self._actRequested = {}
                                                                                                       
    # Receive the data from HKP core which has the connection with the hardware.
    # From HKP only subscribes to the WARN and ALARM
    def callbackHKP(self, ch, method, properties, body):
        l = body.decode().split(',')
        print(f'ALARM or WARNING Receinving from HKP: {l}')
    
    def callbackDT(self, ch, method, properties, body):
        res = body.decode().split(';')
        print(f'Receinving from DTK: {ch} - {res}')
        #l = [2|3];<actionId>;[msg]
        resCode = giapi.HandlerResponse.COMPLETED if res[0] == "2" else giapi.HandlerResponse.ERROR
        self._actRequested[int(res[1])]['response']=resCode
        actionId = int(res[1])
        print(f"actionId: {actionId}")
        if (time.time() - self._actRequested[actionId]['t']) > 0.300: 
            print(f"Responds postCompletionInfo {resCode}")
            self._actRequested[actionId]['numAct'] -= 1;
            if self._actRequested[actionId]['numAct'] == 0: 
               giapi.CommandUtil.postCompletionInfo(actionId, giapi.HandlerResponse.create( resCode))
    
    def callbackDTH(self, ch, method, properties, body):
        l = body.decode().split(',')
        print(f'Receinving from DTH: {ch} - {l}')

    def callbackGiapi(self, actionId, sequenceCommand, activity, config):
        # TODO. I would have to do the logic of the 300 milliseconds
        t = time.time()
        try:
           print(f'callGiapi python function {actionId} - {sequenceCommand} {activity} ')
           print([f"{str(k)} : {config.getValue(k)}" for k in config.getKeys()])
           for k in config.getKeys():
               # TODO. It is necessary to do a regular expression instead of using split
               # It is necessary to know if the apply detector will consume more than 300 milisenconds 
               # in that case, it would be necessary to reponse with STARTED
               if (sequenceCommand == giapi.command.SequenceCommand.APPLY):
                   keys = k.split(':')
                   if keys[1] == 'dc':
                       dc = keys[2]
                       det= self._dtkProd if (dc == 'k') else self._dthProd
                       # The detector process will execute the order and will call the result using rabbitMq
                       self._actRequested[actionId] = {'t' : t, 'response' : None, 'numAct':1}
                       det.sendMessage(self._routingDetPro, f"{actionId};{keys[3]};{config.getValue(k)}")   
               elif sequenceCommand == giapi.command.SequenceCommand.OBSERVE:
                       self._actRequested[actionId] = {'t' : t, 'response' : None, 'numAct':2}
                       self._dtkProd.sendMessage(self._routingDetPro, f"{actionId};observe;k_{config.getValue(k)}")
                       self._dthProd.sendMessage(self._routingDetPro, f"{actionId};observe;y_{config.getValue(k)}")
                       return instDummy.DataResponse(giapi.HandlerResponse.STARTED, "")
               else:
                       print('Not implemented yet')
                       return instDummy.DataResponse(giapi.HandlerResponse.ERROR, "")
               t2 = time.time() - t 
               while (t2 < 0.300):
                   time.sleep(0.010)
                   if self._actRequested[actionId]['response']:
                       break
                       t2 = time.time() - t
               if t2 >= 0.300 or self._actRequested[actionId]['response'] == giapi.HandlerResponse.ERROR:
                   print(f'Error detected time: {t2} seconds')
                   return instDummy.DataResponse(giapi.HandlerResponse.ERROR, "")
        except Exception as e:
            print (e)
            return instDummy.DataResponse(giapi.HandlerResponse.ERROR, "")
        for k in self._actRequested:
            if self._actRequested[k] is None or self._actRequested[k]['response'] == giapi.HandlerResponse.ERROR:
                return instDummy.DataResponse(giapi.HandlerResponse.ERROR, "")
        return instDummy.DataResponse(giapi.HandlerResponse.COMPLETED, "")
                                                                                                       
    def initStatusAndSubs(self):
        # This is the thread to receive alarms from the low level
        self._hkp.connectServer()
        self._hkp.consumer(self._routingHKP, self.callbackHKP)
        # TODO. It changes the Middleware class to inhirit to Thread
        tHKP = Thread(target=self._hkp.startConsumer)
        tHKP.start()
        self._dtkCl.connectServer()
        self._dtkCl.consumer(self._routingDetector, self.callbackDT) 
        tDTk = Thread(target=self._dtkCl.startConsumer)
        tDTk.start()
        self._dthCl.connectServer()
        self._dthCl.consumer(self._routingDetector, self.callbackDT) 
        tDTh = Thread(target=self._dthCl.startConsumer)
        tDTh.start()

        self._dtkProd.connectServer()
        self._dthProd.connectServer()
        # Creating subscription to giapi command
        self._handler = instDummy.InstCmdHandler.create(self._callbackGiapi)
        #self._handlerApply = instDummy.InstCmdHandler.create(self._callbackApply)
        giapi.CommandUtil.subscribeSequenceCommand(giapi.command.SequenceCommand.DATUM, giapi.command.ActivitySet.SET_PRESET_START,self._handler)
        giapi.CommandUtil.subscribeSequenceCommand(giapi.command.SequenceCommand.OBSERVE, giapi.command.ActivitySet.SET_PRESET_START,self._handler)
        print(f'Subscribing APPLY {giapi.CommandUtil.subscribeApply("ig", giapi.command.ActivitySet.SET_PRESET,self._handler)}')
        # Creating status to GIAPI
        #giapi.StatusUtil.createStatusItem("ig:tmc", giapi.type.DOUBLE)
        #giapi.StatusUtil.createStatusItem("ig:tm", giapi.type.DOUBLE)
        #giapi.StatusUtil.createStatusItem("ig:vm", giapi.type.DOUBLE)                                  


if __name__ == '__main__':
    instSeq = InstrumentSequencer()
    instSeq.initStatusAndSubs()
    while (True):
        time.sleep(2)
