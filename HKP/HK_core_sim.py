#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   HK Simulator
"""



from curses import baudrate
import os, sys
sys.path.append("../")
import Libs.SetConfig as sc
from Libs.MsgMiddleware import MsgMiddleware
import time
from time import localtime, strftime 
import random
from HK_def import *


dtvalue_key_list = ["tmc1-temp-a",
                    "tmc1-temp-b",
                    "tmc2-temp-a",
                    "tmc2-temp-b",
                    "tmc3-temp-a",
                    "tmc3-temp-b",
                    "tm-temp-1",
                    "tm-temp-2",
                    "tm-temp-3",
                    "tm-temp-4",
                    "tm-temp-5",
                    "tm-temp-6",
                    "tm-temp-7",
                    "tm-temp-8"]


class HK() :
    def __init__(self, gui=False):
        
        self.gui = gui
        print(f"start HKP  {IAM} !!!")        
        # definition: variables
        global COM_IP, COM_PORT
        global UT_POS, LT_POS
        global TOUT, TSLEEP, CMCWTIME
        global REBUFSIZE, CMCREBUFSIZE
            
        self.comList = ["tmc1", "tmc2", "tmc3", "tm", "vmc", "lt", "ut", "pdu"]
        COM_IP, COM_PORT = [], []
        self.comStatus = [False for _ in range(COM_CNT)]
        
        #for CLI mode
        self.comSocket = [None for _ in range(COM_CNT)]
                
        #for async
        #self.comReader = ["" for _ in range(COM_CNT)]
        #self.comWriter = ["" for _ in range(COM_CNT)]
         
        self.pow_flag = ["OFF" for _ in range(PDU_IDX)]

        TSLEEP = random.choice([1,2,3,4])
        # load ini file
        #self.ini_file = WORKING_DIR + "IGRINS/Config/IGRINS.ini"
        #self.cfg = sc.LoadConfig(self.ini_file)

        
        #read Interval from IGRINS.ini
        self._period = 5
        self._ipAddr = 'localhost'
        self._exchange = 'HKPtoCli'
        self.producter = MsgMiddleware(self._ipAddr, self._exchange, 'direct', False)
        self._routingKey = ["INFO", "WARM", "ALARM"]
        
    # --------------------------------------------------
    # CLI
    def connect_to_component(self, nCom):
            print(f" Simulating connection to hardware ")
            time.sleep(1)
            self.comStatus[nCom] = True
            print(f' Connected to simulator hardware ')
             
    def connectRabbitMq(self):
            self.producter.connectServer()
    
    def re_connect_to_component(self, nCom):
        #time.sleep(TOUT)
        self.cur_err[nCom] = True
        self.logwrite(BOTH, self.comList[nCom] + " is trying to connect again")
        self.connect_to_component(nCom)
           
    # CLI
    def close_component(self, nCom):
        self.comStatus[nCom] = False
        
        
    # CLI, TMC-Get SetPoint
    def get_setpoint_fromTMC(self, nCom, nPort):
        cmd = "SETP? %d" % nPort
        cmd += "\r\n"
        return self.socket_send_recv(nCom, nPort, cmd)


    # CLI, TMC-Heating Value
    def get_heating_power(self, nCom, nPort):
        cmd = "HTR? %d" % nPort
        cmd += "\r\n"
        return self.socket_send_recv(nCom, nPort, cmd)
    
    
    # CLI, TMC-Heating(Manual) Get Value
    def get_heating_power_manual(self, nCom, nPort):
        cmd = "MOUT? %d" % nPort
        cmd += "\r\n"
        return self.socket_send_recv(nCom, nPort, cmd) 
    
    
    # CLI, TMC-Heating(Manual) Set Value
    def SetHeatingValue_manual(self, nCom, nPort, value):
        cmd = "MOUT %d,%f" % (nPort, value)
        cmd += "\r\n"
        return self.socket_send_recv(nCom, nPort, cmd)
    

    # CLI, TMC-Monitorig
    def get_value_fromTMC(self, nCom, sPort):  
        cmd = "KRDG? " + sPort
        cmd += "\r\n"
        return self.socket_send_recv(nCom, sPort, cmd)

    # CLI, TM-Monitorig
    def get_value_fromTM(self, nPort):
        cmd = "KRDG? %d" % nPort
        cmd += "\r\n"
        return self.socket_send_recv(TM, nPort, cmd)

    # CLI, Vaccum monitoring
    #PR1 - MicroPirani, PR2/PR5 - Cold Cathode, PR3 - both (3 digits), PR4 - both (4 digits)
    def get_value_fromVM(self):
        cmd = "@253PR3?;FF"
        cmd += "\r\n"
        return self.socket_send_recv(VMC, 1, cmd)

    # Socket function
    def socket_send_recv(self, nCom, port, cmd):
        print(f'lalalla')
        try:         
            num = random.random()
            log=""
            print(f'num: {num} {port} {self.comList} {self.comList[nCom]}')
            if port == "A" or port == "B":
                print(f'num33: {num}')
                log += "send: %s %s >>> %s" % (self.comList[nCom], port, cmd)
            else:
                log += "send: %s %d >>> %s" % (self.comList[nCom], port, cmd)
            print(f'num22: {num}')
            self.logwrite(BOTH, log)
            print(f'{log}')
        
            if cmd.find("MOUT ") == 0:
                d1, d2 = cmd.split(',')
                print("set:",str(float(d2)))
                return None
            
            info = random.random()
                        
            if port == "A" or port == "B":
                log += "recv %s %s <<< %s" % (self.comList[nCom], port, info)
            else:
                log += "recv %s %d <<< %s" % (self.comList[nCom], port, info)
            self.logwrite(LOGGING, log)

            return info
            

        except Exception as e:
            print(e)
            if not self.gui:
                if nCom == VMC:
                    message = "%s sending fail (%s)" % (CLASS_NAME, self.comList[nCom])
                elif port == "A" or port == "B":
                    message = "%s sending fail (%s port %s)" % (CLASS_NAME, self.comList[nCom], port)
                else:
                    message = "%s sending fail (%s port %d)" % (CLASS_NAME, self.comList[nCom], port)
                self.logwrite(CMDLINE, message)
                return None

            self.comStatus[nCom] = False
            self.re_connect_to_component(nCom)
            
        

    # CLI
    def initPDU(self):
        if not self.comStatus[PDU]:
            print(f' you have to connect first, please {PDU} ')
            return 
        
        try:
            cmd = "@@@@\r"
            #self.comSocket[PDU].send(cmd.encode())
            log = "send: %s >>> %s" % (self.comList[PDU], cmd)
            self.logwrite(LOGGING, log)
            
            #res = self.comSocket[PDU].recv(REBUFSIZE)
            #log = "recv %s <<< %s" % (self.comList[PDU], res.decode())
            log = "recv %s <<< %s" % (self.comList[PDU], "pdu initialized")
            self.logwrite(LOGGING, log)
            
            cmd = "DN0\r"   #need to check!!!
            self.power_status(cmd) 
                
            if self.gui:
                self.logwrite(BOTH, "powctr init is completed")
            else:
                self.logwrite(CMDLINE, CLASS_NAME + " powctr init is completed (" + self.comList[PDU] + ")")
                    
        except:
            if self.gui:
                self.logwrite(BOTH, "powctr init is error")
                   
                self.comStatus[PDU] = False
                self.re_connect_to_component(PDU)
            else:
                self.logwrite(CMDLINE, CLASS_NAME + " sending fail (" + self.comList[PDU] + ")")
        
    def getPowerStatus(self):
        return self.pow_flag
                    
    def power_status(self, cmd):
        if not self.comStatus[PDU]:
            print(f' you have to connect first, please')
            return      
        
        try:
            #self.comSocket[PDU].send(cmd.encode())
            log = "send: %s >>> %s" % (self.comList[PDU], cmd)
            self.logwrite(BOTH, log)
            time.sleep(TSLEEP)
            #res = self.comSocket[PDU].recv(REBUFSIZE)
            #sRes = res.decode()
            sRes = "OUTLET 1 ON"
            log = "recv %s <<< %s" % (self.comList[PDU], sRes)
            self.logwrite(BOTH, log)
            
            # check PDU status
            for i in range(PDU_IDX):
                #if sRes.find("OUTLET %d ON" % (i + 1,)) >= 0:
                if i % 2 == 0:
                    self.pow_flag[i] = "ON"
                else:
                    self.pow_flag[i] = "OFF"
        except Exception as e:
                print (e)
                self.logwrite(BOTH, "powctr sending fail")
                   
                self.comStatus[PDU] = False
                self.re_connect_to_component(PDU)

    def logwrite(self, option, event):
        '''
        Function that write to file for Logging
        event : Logging Sentence
        option :  LOGGING(1) - Write to File
                  CMDLINE(2) - Write to Command Line
                  BOTH(3) - Wrte to File and Command Line
        '''
        #if option == CMDLINE:
        #    print(event)
        #else:
        #    fname = strftime("%Y%m%d", localtime())+".log"
        #    f_p_name = self.mainlogpath+fname
        #    if os.path.isfile(f_p_name):
        #        file=open(f_p_name,'a+')
        #    else:
        #        file=open(f_p_name,'w')
            
        #    if option == LOGGING:
        #        file.write(strftime("[%Y-%m-%d %H:%M:%S]", localtime()) + ": " + event + "\n")
        #        file.close()
        
        #    elif option == BOTH:
        #        file.write(strftime("[%Y-%m-%d %H:%M:%S]", localtime()) + ": " + event + "\n")
        #        file.close()
        print(event)

    def main(self):
        for i in range(COM_CNT):
           self.connect_to_component(i)
        self.connectRabbitMq()
        self.initPDU()
        while (True):
            for i in range(COM_CNT):
               msg = f"tmc,{self.get_value_fromTMC(i,'A')}"
               self.producter.sendMessage([self._routingKey[0]],f"tmc,{self.get_value_fromTMC(i,'A')}")
               self.producter.sendMessage([self._routingKey[0]],f"tm,{self.get_value_fromTM(i)}")
               self.producter.sendMessage([self._routingKey[0]],f'vm,{self.get_value_fromVM()}')
               self.producter.sendMessage([self._routingKey[1]],f'powerStatus,{self.getPowerStatus()}')
               time.sleep(1)
            time.sleep(self._period)

if __name__ == '__main__':
    try:
        client = HK()
        client.main()
    except KeyboardInterrupt:
        print('Interrupted ')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


