#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Created on Jun 28, 2022

Modified on Nov 7, 2022 

@author: hilee

This code was created by Fran. R from the DT_core.py. 
I showed this code to hye-In as an example how the RabittMQ 
could be used with the MiddleWare.py. This simulation code
implements the observe command executed Inst.Seq which was
invoked by the SeqExec.
"""

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DT_def import *
import time
from time import localtime, strftime
import numpy as np
from astropy.io import fits

import Libs.SetConfig as sc
from Libs.MsgMiddleware import MsgMiddleware
from Libs.logger import *
from threading import Thread

class DT():
    def __init__(self, detName):
        
        self.log = LOG(WORKING_DIR + "IGRINS", IAM)
        self.iam = "DTsim"
        self.logwrite(INFO, "start DCS core!!!")

        self._ipAddr = 'localhost'
        self._exchangeProd = f'DT{detName}ToCli'
        print(f'detname: {self._exchangeProd} ')
        self._producter = MsgMiddleware(self._ipAddr, self._exchangeProd, 'direct', False)
        #self._producter = MsgMiddleware('localhost', 'DTKToCli', 'direct', False)
        self._rKeysProd = ["COMPLETED","INFO", "WARM", "ALARM"]

        self._exchangeCl = f"CliToDT{detName}"
        print(self._exchangeCl)
        self._consumer = MsgMiddleware(self._ipAddr, self._exchangeCl, 'direct', True)
        self._rKeysCl = ["CMD"]
        self.fits_path = './fits-dir/'
        self._t_exp = 1.634
        #--------------------------------------------
        
    def __del__(self):
        self.logwrite(INFO, "DTP core closing...")
        self.logwrite(INFO, "DTP core closed!")
        
    def logwrite(self, level, message):
        level_name = ""
        if level == DEBUG:
            level_name = "DEBUG"
        elif level == INFO:
            level_name = "INFO"
        elif level == WARNING:
            level_name = "WARNING"
        elif level == ERROR:
            level_name = "ERROR"
        
        msg = "[%s:%s] %s" % (self.iam, level, message)
        self.log.send(level, msg)
        
    def initialize2(self, dc_idx):
        print(f'{dc_idx} - {CMD_INITIALIZE2} ')
        
    def downloadMCD(self, dc_idx):
        print(f'{dc_idx} - {CMD_DOWNLOAD} ')

    
    def set_detector(self, dc_idx, channel):
        msg = "%s %d %d" % (CMD_SETDETECTOR, MUX_TYPE, channel)
        print(f'Set detector, sending message {dc_idx} { msg} ')
          
    def set_fs_param(self, dc_idx, exptime):
        #fsmode
        print(f'{dc_idx} {CMD_SETFSMODE} + " 1"')    
        
        #setparam
        param = " 1 1 1 %f 1" % exptime
        print(f'{dc_idx}, {CMD_SETFSPARAM}  {param}')
    

    def setExposureTime(self, t_exp):
        msg = "%s 0" % CMD_ACQUIRERAMP
        print(f'Received setExposureTime: {t_exp} ')
        self._t_exp = t_exp


    def observe(self, datalabel, image_name):
        print(f'observe {datalabel} - {image_name} - Exposing : {self._t_exp} ')
        t = time.time()
        n = np.ones((3, 3))
        n2 = np.ones((100, 100))
        n3 = np.ones((10, 10, 10))
        primary_hdu = fits.PrimaryHDU(n)
        image_hdu = fits.ImageHDU(n2)
        image_hdu2 = fits.ImageHDU(n3)
        hdul = fits.HDUList([primary_hdu, image_hdu, image_hdu2])
        hdr = hdul[0].header
        hdr['OBSERVER'] = 'Hwi Igrings2'
        hdr['COMMENT'] = 'This is an example'
        hdr['DATALABEL'] = datalabel
        time.sleep(self._t_exp)
        if os.path.exists(f"/tmp/images/{image_name}"):
           os.remove(f"/tmp/images/{image_name}")
        hdul.writeto(f"/tmp/images/{image_name}")
        return f"/tmp/images/{image_name}"
    
    def acquireramp(self, dc_idx):
        msg = "%s 0" % CMD_ACQUIRERAMP
        print(f'{dc_idx}, {msg}')
          
    def alive_check(self, dc_idx):
        print(f'{dc_idx}, "alive?"')
        
    def stop_acquistion(self, dc_idx):        
        print(f'{dc_idx} - {CMD_STOPACQUISITION} ')

    def callbackClient(self, ch, method, properties, body):
        l = body.decode().split(';')
        #actionId;action;value-parameter1}
        print(f'Receiving {l} ')
        if l[1] == "setExpTime":
           self.setExposureTime(float(l[2]))
           self._producter.sendMessage([self._rKeysProd[0]], f"2;{l[0]}")
        elif l[1] == "observe":
           #TODO. Verificate high level the datalabel
           #path = self.observe(l[2], 'IG20221121_1')
           path = self.observe(l[2], l[2])
           self._producter.sendMessage([self._rKeysProd[0]], f"2;{l[0]};{path}")
             
    def connectRabbitMq(self):                 
        self._producter.connectServer()  
        self._consumer.connectServer()
        self._consumer.consumer(self._rKeysCl, self.callbackClient)
        t = Thread(target=self._consumer.startConsumer)
        t.start()
        while (True):
            time.sleep(1)

    def main(self):
        self.connectRabbitMq()

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) < 2 and sys.argv[1] != 'K' and  sys.argv[1] != 'H':
        print('Please, you should provide a correct argument. Example python DT_sim_,py K ')
        sys.exit()
    dt = DT(sys.argv[1])
    dt.main()

