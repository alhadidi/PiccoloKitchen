# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:50 2019

@author: Alejandro Garcia

Script to create the dashboard about actual status of the kitchen user. Here it is 
designed the page structure, all callback functions are defined in the main script.


"""

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.io as pio
import plotly.graph_objs as go

file_name=('Data/kitchen_status.csv')
pio.templates.default = "plotly_dark"
colors=px.colors.diverging.Tealrose
data=pd.read_csv(file_name).round(2)
graph_height=520

#Grpah definition
colors ={
        'background':'black',#'rgba(30,30,30,0.2)',
        'text': 'white',
        'title': 'white',
        'right': 'rgba(128, 128, 128, 0.2)',
        'kitchen_top': 'rgba(128, 128, 128, 0.5)',
        'led':'rgba(128, 128, 128, 0.1)',
        'temp':'rgb(248, 160, 126)',
        'temp_fill':'rgba(248, 160, 126,0.1)',
        'hum':'rgb(133, 196, 201)',
        'hum_fill':'rgba(133, 196, 201,0.1)',
        'lit':'rgb(254, 252, 205)',
        'lit_fill':'rgba(254, 252, 205,0.1)',
        'sound_right':'rgb(76, 200, 163)',
        'sound_right_med':'rgba(76, 200, 163,0.2)',
        'sound_right_low':'rgba(76, 200, 163,0.1)',     
        'sound_left':' rgb(56, 178, 163)',
        'sound_left_med':' rgba(56, 178, 163,0.2)',
        'sound_left_low':' rgba(56, 178, 163,0.1)',
        }

temp={'data':[go.Scatter(                         
              y= data.iloc[-200::2,4].tolist(),
              x=data.iloc[-300::3,0].tolist(),
              line={'color':colors['temp']},
              fill='tozeroy',
              fillcolor=colors['temp_fill'],
             )],
     'layout': {
             'yaxis':{'fixedrange':False,
                      'range':[10,35],
                      'tickfont':{'size':14},
                      'gridcolor':colors['background'],
                      'title':'(ºC)'},
             'xaxis':{'nticks':7,
                      'tickangle':15,
                      'tickfont':{'size':14},
                      'gridcolor':colors['background']},
             'title': {'text':'Temperature (ºC)',
                       'x':0.1,
                       },
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {  'size':15,
                        'color': colors['text']},
             'height':500,
             
                }
}
hum={'data':[go.Scatter(             
                  y= data.iloc[-300::3,5].tolist(),
                  x=data.iloc[-300::3,0].tolist(),
                  line={'color':colors['hum']},
                  fill='tozeroy',
                  fillcolor=colors['hum_fill'],
                  mode='lines'
                 )],
     'layout': {
             'yaxis':{'fixedrange':False,
                      'range':[36,52],
                       'title':'(%)'},
             'xaxis':{'nticks':7,
                      'tickangle':15,
                      'tickfont':{'size':14}},
             'title': {'text':'Humidity (%)',
                       'x':0.1,
                       },
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {  'size':15,
                        'color': colors['text']},
             'height':500,
                }
}  
lit={'data':[go.Scatter(             
              y= data.iloc[-200::2,6].tolist(),
              x=data.iloc[-300::3,0].tolist(),
              line={'color':colors['lit']},
              fill='tozeroy',
              fillcolor=colors['lit_fill'],
             )],
     'layout': {
             'yaxis':{'fixedrange':False,
                      'range':[520,575],
                       'title':'(Lux)'},
             'xaxis':{'nticks':7,
                      'tickangle':15,
                      'tickfont':{'size':14}},
             'title': {'text':'Light levels (Lux)',
                       'x':0.1,
                       },
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {  'size':15,
                        'color': colors['text']},
             'height':500,
             }
} 
             
##Sound graphs
sound_right={
    'data':[  go.Scatter(             
              y= [10]*1000,
              x=data.iloc[:,0].tolist(),
              line={'color':colors['sound_right_low']},
              fill='tozeroy',
              fillcolor=colors['sound_right_low'],
              mode='none',
              name="Low Level"
             ),
             go.Scatter(             
              y= [15]*1000,
              x=data.iloc[:,0].tolist(),
              line={'color':colors['sound_right_med']},
              fill='tonextx',
              fillcolor=colors['sound_right_med'],
              mode='none',
              name='Medium level'
             ),
             go.Scatter(             
              y= data.iloc[:,2].tolist(),
              x=data.iloc[:,0].tolist(),
              line={'color':colors['sound_right']},
           #   fill='tozeroy',
          #    fillcolor=colors['lit_fill'],
             name='Sound level'
             )],
     'layout': {
          #  'yaxis':{'fixedrange':True,
          #            'range':[520,575]},
             'xaxis':{'nticks':15,
                      'tickangle':30,
                      'tickfont':{'size':14}},
             'title': {'text':'Sound Level Right Side',
                       'x':0.1,
                       },
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {  'size':15,
                        'color': colors['text']},
             'height':400,
             }
}    
sound_left={
    'data':[  go.Scatter(             
              y= [10]*1000,
              x=data.iloc[:,0].tolist(),
              line={'color':colors['sound_left_low']},
              fill='tozeroy',
              fillcolor=colors['sound_left_low'],
              mode='none',
              name="Low Level"
             ),
             go.Scatter(             
              y= [15]*1000,
              x=data.iloc[:,0].tolist(),
              line={'color':colors['sound_left_med']},
              fill='tonextx',
              fillcolor=colors['sound_left_med'],
              mode='none',
              name='Medium level'
             ),
             go.Scatter(             
              y= data.iloc[:,2].tolist(),
              x=data.iloc[:,0].tolist(),
              line={'color':colors['sound_left']},
           #   fill='tozeroy',
          #    fillcolor=colors['lit_fill'],
             name='Sound level'
             )],
     'layout': {
            'yaxis':{'showgrid': False},
             'xaxis':{'nticks':15,
                      'tickangle':30,
                      'tickfont':{'size':14},
                      'showgrid': False},
             'title': {'text':'Sound Level Left Side',
                       'x':0.1,
                       },
             'plot_bgcolor':colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {  'size':15,
                        'color': colors['text']},
             'height':400,
             }
}  
             
Enviromental_layout=html.Div([
                        html.H5(className='tab-title',
                                children=['Room Environment']),
                        html.Div(className='row',children=[
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='temperature-graph',className='',
                                                      figure=temp)
                                        ]),
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='light-graph',
                                                      figure=lit)               
                                        ]),                               
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='humidity-graph',
                                                figure=hum)
#      figure=px.line(data,x='Time',y='Humidity',title='Humidity (%)',range_x=[0,100],range_y=[40,45],color_discrete_sequence=['rgb(133, 196, 201)',''],height=graph_height))
                                                                               
                                        ]), 
                               ]),
                        html.Br(),
                        html.Div(className='row eleven columns',children=[
                            html.Div(className='six columns',children=[
                                            dcc.Graph(id='humidity-graph',
                                                      figure=sound_right)
                                ]),
                             html.Div(className='six columns',children=[
                                            dcc.Graph(id='humidity-graph',
                                                      figure=sound_left)
#                                                      figure=px.line(data,x='Time',y='Sound 2',title='Sound Level Left Side',range_y=[0,30],color_discrete_sequence=['rgb(56, 178, 163)',''],height=graph_height))
                                ]),
                        ]),
])