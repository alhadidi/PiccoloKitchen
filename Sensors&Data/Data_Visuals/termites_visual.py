# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:29:10 2019

Script to create the dashboard about enviromental data of the kitchen using terMITes. Here it is 
designed the page structure, all callback functions are defined in the main script.

@author: Alejandro Garcia
"""

import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

# --------------------------------------------------------------------------------------
""" Subplots definition """

liv_ter=pd.read_csv('C:/Users/Alejandro/Desktop/MIT Media Lab/codes/terMITes/csv_serial.csv')
colors ={
        'background':'black',
        'text': 'white',
        'title': 'white',
        'right': 'rgba(128, 128, 128, 0.2)',
        'kitchen_top': 'rgba(128, 128, 128, 0.5)',
        'led':'rgba(128, 128, 128, 0.1)'
        }
 
temp={'data':[go.Scatter(                         
              y= liv_ter.iloc[-1000:,4].tolist(),
              line={'color':'red'},
              fill='toself',
              fillcolor='rgba(255,102,102,0.1)',
             )],
     'layout': {
             'title': 'Temperature',
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {
                        'color': colors['text']},
             'height':300,
                }
}
hum={'data':[go.Scatter(             
                  y= liv_ter.iloc[-1000:,6].tolist(),
                  line={'color':'blue'},
                  fill='toself',
                  fillcolor='rgba(153,153,255,0.1)',
            #                      mode='lines+markers'
                 )],
     'layout': {
             'title': 'Humidity',
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {
                        'color': colors['text']},
             'height':300,
                }
}  
lit={'data':[go.Scatter(             
              y= liv_ter.iloc[-1000:,5].tolist(),
              line={'color':'yellow'},
             # fill='tozeroy',
              fillcolor='rgba(230,255,0,0.1)'
             )],
     'layout': {
             'title': 'Light',
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {
                        'color': colors['text']},
             'height':300,
                }
} 

# --------------------------------------------------------------------------------------
""" Layout """

terMITes_layout=html.Div([
        html.Div([
                html.H5(className='development-title',
                        children=['Page under development.']),
                            
                        ]),
        html.Div(className='eight columns',children=[

        dcc.Graph(id='temp',className='graph-container', 
                  figure=temp             
                ),
        dcc.Graph(id='hum',className='graph-container', 
                  figure=hum             
                ),
        dcc.Graph(id='lit',className='graph-container', 
                  figure=lit             
                )        ]),
        ]),