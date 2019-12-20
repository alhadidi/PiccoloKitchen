# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:55:58 2019
Script for taking the data from the sensors connected to and arduino + 1 termite

@author: Alejandro
"""
import serial
from datetime import datetime
import pandas as pd
#Serial imports
ser = serial.Serial(
    port='COM4',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        )
ter = serial.Serial(
    port='COM8',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        )
kitchen_status=pd.DataFrame(columns=['Time',
                                     'Position','Sound 1','Sound 2','Temperature','Humidity','Light', ##Kitchen top
                                     'Position Back','N Mov Back','N Back pos','N Back total',        ## Back cabinet
                                     'Position Front','N Mov Front','N Front pos','N Front total']);  ## Front cabinet
##time.sleep(5.0)
while True:
    data=(ser.readline().decode('utf-8').split('/'))
    termite=(ter.readline().decode('utf-8'))
    try:
        temp=termite.replace(' = ',':').split(' ')[4].split(':')[1]
        hum=termite.replace(' = ',':').split(' ')[6].split(':')[1]
        lit=termite.replace(' = ',':').split(' ')[5].split(':')[1]
    except:
      print(termite)

    try: 
        kitchen_status=kitchen_status.append({'Time':datetime.now().strftime('%H:%M:%S'),
                                              'Position': data[0],
                                              'Sound 1': data[1],'Sound 2': data[2],
                                              'Temperature': temp,'Humidity':hum,'Light':lit,
                                              'Position Back': data[3],'N Mov Back':data[4],
                                              'N Back pos': data[5],'N Back total':data[6],
                                              'Position Front': data[7],'N Mov Front':data[8] ,
                                              'N Front pos': data[9],'N Front total':data[10].strip("\r\n")}
        ,ignore_index=True)
    except:
        print(data)

    kitchen_status.to_csv('kitchen_status_21_11.csv',index=False)


ser.close()
ter.close()

