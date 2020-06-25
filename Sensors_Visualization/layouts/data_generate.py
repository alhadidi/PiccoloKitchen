# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:09:22 2020

@author: Alejandro
"""
import pandas as pd
from math import sin,cos
import random
t=pd.DataFrame(columns=['Temperature','Humidity','Light']
)
for i in range(890):
      t=t.append({'Temperature':26+abs(sin(i))+random.uniform(0,2),'Humidity':40+abs(cos(i))+random.uniform(2,5),'Light':550+sin(i)+random.uniform(8,15)},ignore_index=True
     )
      
      
      

