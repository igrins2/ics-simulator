#!/usr/bin/env python3
import cppyy
import os, time, sys
from multiprocessing import Pipe, Process
from threading import Thread
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


#class HKPcc(Process):
class HKPcc:
    def __init__(self):
        Process.__init__(self)
        self._ipAddr = 'localhost'
        self._id = 'HKP-id'
        self._exchange = 'HKPtoCli'
        self._routing = ["INFO", "WARM", "ALARM"]
        self._hkp = MsgMiddleware(self._ipAddr, self._exchange, 'direct') # TODO. Currently only admit direct. if we want another, we should implement it.
        # This line is necessary because the cppyy is not managing the life cycle of the object. 
        # Without this line, when you InstCmdHandler.create using the function directly self.callbackGiapi
        # you will receive the following error   what():  TypeError: callable was deleted
        #self._callbackGiapi = self.callbackGiapi
        self._handler = None


    # Receive the data from HKP core which has the connection with the hardware. 
    def callbackRabbitmq(self, ch, method, properties, body):
        #print(f"Receive, body:{body}, method:{method}, ch: {ch}, properties: {properties}")
        l = body.decode().split(',')
        if (l[0] == "vm" or l[0] == "tm" or l[0] == "tmc" ):
            print(f'Updating status giapi ig:{l[0]} -> {l[1]} ')
            giapi.StatusUtil.setValueAsFloat(f'ig:{l[0]}', float(l[1]))
            giapi.StatusUtil.postStatus(f"ig:{l[0]}")
 
    def initStatusAndSubs(self):
        # Creating connection as consumer with igrings HKP component
        self._hkp.connectServer()
        self._hkp.consumer(self._routing, self.callbackRabbitmq)
        # Creating status to GIAPI
        print('Creating the status')
        status = giapi.StatusUtil.createStatusItem("ig:tmc", giapi.type.FLOAT)
        print(f" ig:tmc -> c {status} - {giapi.status.OK} ")
        status = giapi.StatusUtil.createStatusItem("ig:tm", giapi.type.FLOAT)
        print(f" ig:tm -> c {status} - {giapi.status.OK} ")
        status = giapi.StatusUtil.createStatusItem("ig:vm", giapi.type.FLOAT)
        print(f" ig:vm -> c {status} - {giapi.status.OK} ")
        #giapi.StatusUtil.createStatusItem("ig:vm", giapi.type.DOUBLE)

    def run(self):
        try:
            # communication using rabbitmq
            self.initStatusAndSubs()
            self._hkp.startConsumer()
            #t = Thread(target=self._hkp.startConsumer)
            #t.run()
            #while(True):
                # Here should put the logic to send with the InstrumentSequencer
            #    time.sleep(1)

        except Exception as e:
            print("Error on Clien HKP")
            print (e)


if __name__ == '__main__':
   hkpcc = HKPcc()
   hkpcc.run()
   
