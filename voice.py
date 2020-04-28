# -*- coding: utf-8 -*-
import subprocess
import socket
import string
import os
import random
import numpy as np
from numpy.random import *
import time

host = '127.0.0.1' 
#host = "localhost"
port = 10500


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("input host port")
sock.connect((host, port))
print("connected")

data =""
killword =""

while True:
    #print(data)
    
    if '</RECOGOUT>\n.' in data:
        strTemp = ""
        for line in data.split('\n'):
            index = line.find('WORD="')
            if index != -1:
                line_ori = line
                line = line[index+6:line.find('"',index+6)]
                if line == "[s]" or line == "[/s]":
                    continue
                cmscore = line_ori[-6:-3]
                strTemp = str(line)
                print(cmscore)
                print(strTemp)
                cmscore = int(cmscore)
                if cmscore == 000:
                    cmscore = 1000
            if strTemp == 'テレビオン' and int(cmscore) > 700:
                #args = ["-p", "-g17", "-f", "codes", "light:on"]
                subprocess.Popen("python3 irrp.py -p -g17 -f codes light:on", shell = True)
                print("ON")
                break

            elif strTemp == 'テレビオフ'and int(cmscore) > 900:
                print("OFF")
                break

            elif strTemp == 'テレビいちばん' and int(cmscore) > 850:
                subprocess.Popen("python3 irrp.py -p -g17 -f ch1 light:on", shell = True)
                print("CH1")
                break

            elif strTemp == 'テレビにばん' and int(cmscore) > 850:
                subprocess.Popen("python3 irrp.py -p -g17 -f ch2 light:on", shell = True)
                print("CH2")
                break

            elif strTemp == 'テレビさんばん' and int(cmscore) > 850:
                subprocess.Popen("python3 irrp.py -p -g17 -f ch3 light:on", shell = True)
                print("CH3")
                break
            
            elif strTemp == 'テレビよんばん' and int(cmscore) > 800:
                subprocess.Popen("python3 irrp.py -p -g17 -f ch4 light:on", shell = True)
                print("CH4")
                break

            elif strTemp == 'テレビごばん' and int(cmscore) > 850:
                subprocess.Popen("python3 irrp.py -p -g17 -f ch5 light:on", shell = True)
                print("CH5")
                break

            elif strTemp == 'テレビろくばん' and int(cmscore) > 900:
                subprocess.Popen("python3 irrp.py -p -g17 -f ch6 light:on", shell = True)
                print("CH6")
                break
            
            elif strTemp == '消灯して' and int(cmscore) > 990:
                subprocess.Popen("python3 irrp.py -p -g17 -f lightoff light:on", shell = True)
                break

            elif strTemp == '点灯して' and int(cmscore) > 990:
                subprocess.Popen("python3 irrp.py -p -g17 -f lighton light:on", shell = True)
                break

            elif strTemp == 'エアコン付けて' and int(cmscore) > 990:
                subprocess.Popen("python3 irrp.py -p -g17 -f danbou light:on", shell = True)
                break

            elif strTemp == 'エアコン消して' and int(cmscore) > 990:
                subprocess.Popen("python3 irrp.py -p -g17 -f airoff light:on", shell = True)
                break

            else:
                pass
            data = ""
            
    else:
        data += str(sock.recv(1024).decode('utf-8'))
