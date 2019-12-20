# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:55:58 2019
Script for taking the data from the sensors connected to and arduino + 0 terMITe
@author: Alejandro
"""

import serial
from datetime import datetime
import pandas as pd
import plotly.subplots as subplots
import pandas as pd
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
from plotly.offline import plot
#Serial imports
ser = serial.Serial(
        
    port='COM4',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    )
kitchen_status=pd.DataFrame(columns=['Time','Sound 1','Sound 1 Level',#'Sound 2',
                                     'Distance Right','Distance Left','User Position',
                                     'Position Back','N Mov Back','N Back total','N Back pos',
                                     'Position Front','N Mov Front','N Front total','N Front pos']);
date=datetime.now().strftime('%Y-%m-%d_%H-%M')
file_name='kitchen_status_T0_'+date+'.csv'
#file_name_txt='kitchen_status_T0_'+date+'.txt'
##time.sleep(5.0)
while True:
    data=(ser.readline().decode('utf-8'))
#    print(data)
#    data=data.split('/')
    try:
        data=data.split(',')
    except:
        print('n')
    try: 
       kitchen_status=kitchen_status.append({'Time':datetime.now().strftime('%H:%M:%S'),
                                              'Sound 1': data[0],
                                              'Sound 1 Level': data[1],#'Sound 2': data[2],
                                              'Distance Right':data[2],'Distance Left':data[3],'User Position':data[4],
                                              'Position Back': data[5],'N Mov Back':data[6],
                                              'N Back total': data[7],'N Back pos':data[8],
                                              'Position Front': data[9],'N Mov Front':data[10] ,
                                              'N Front total': data[11],'N Front pos':data[12].strip("\r\n")}
        ,ignore_index=True)

    except:
        print('error')

    kitchen_status.to_csv(file_name,index=False)
#    kitchen_status.to_txt(file_name_txt,index=False)


ser.close()
