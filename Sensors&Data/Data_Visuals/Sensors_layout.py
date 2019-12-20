# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:32:10 2019


Script to create the dashboard about historical data of the kitchen user. Here it is 
designed the page structure, all callback functions are defined in the main script.

@author: Alejandro Garcia
"""

import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

import plotly.io as pio

# --------------------------------------------------------------------------------------
""" Data Read """

file_name='C:/Users/Alejandro/Desktop/MIT Media Lab/codes/full_kitchen_sensor/Data/kitchen_status.csv'
data=pd.read_csv(file_name)
variables=data.columns
data_tras=data.T
data_table=data_tras.iloc[:,10:15]
data_table.insert(0,'Variables',variables,True)
data_tras.insert(0,'Variables',variables,True)
variables_table=['Position','Position Back','Position Front','Temperature','Humidity','Light']

# --------------------------------------------------------------------------------------
""" Functions """

def generate_table_user(dataframe,variables):
    return html.Table(
        # Header
      
        [html.Tr([html.Th(col) for col in dataframe.columns])] + 
        # Body  
        [html.Tr([html.Td(dataframe.loc[i][col]) for col in dataframe.columns]) for i in variables]
    )

pio.templates.default = "plotly_white"


# --------------------------------------------------------------------------------------
""" Layout """

Sensors_layout=html.Div([
      
        html.Div(className='row four columns container',children=[
                html.Div(className='row dropdown-container',children=[
                    html.Label('Variables: '),
                    dcc.Dropdown(className='eight columns',id='var-dropdown',options=[{'label':x, 'value':x} for x in variables],
                                value='Position')
                ]),
                dcc.Graph(id='main-graph', className='graph',                                 
                          ),
                dcc.RangeSlider(id='first-slider',
                                min=0,max=900, step=1, value=[0,900])]), 
        html.Div(className='row four columns container',children=[
            html.Div(className='row dropdown-container', children=[
                    html.Div(className='six columns', children=[
                        html.Label('Variable X:'),
                        dcc.Dropdown(className='',id='bar-sensor-x',options=[{'label':'Position Back', 'value':'Position Back'},
                                                                      {'label':'Position Front', 'value':'Position Front'},
                                                                      {'label':'Position', 'value':'Position'}],
#                                                                      {'label':'Sound 1', 'value':'Sound 1'},
#                                                                      {'label':'Sound 2', 'value':'Sound 2'}],#for x in variables, ##Make it General
                                                        value='Position Back')
                        ]),   
                    html.Div(className='six columns', children=[              
                        html.Label('Variable Comp:'),
                        dcc.Dropdown(id='bar-sensor-compare',options=[{'label':'Position Back', 'value':'Position Back'},
                                                                      {'label':'Position Front', 'value':'Position Front'},
                                                                      {'label':'Position', 'value':'Position'}],
#                                                                      {'label':'Sound 1', 'value':'Sound 1'},
#                                                                      {'label':'Sound 2', 'value':'Sound 2'}],
                                                        value='Position')]),
    #                    html.Br()
#                    dcc.RangeSlider(id='second-slider',
#                                min=0,max=900, step=1, value=[0,900])]), 
                    
            ]),
            html.Div(className='', children=[
                    dcc.Graph(id='bar-sensor')])
            ]),
     
#        html.Br(),
        html.Div(className='row four columns container',children=[

            html.Div(className='row dropdown-container', children=[
                    html.Div(className='six columns', children=[
                        html.Label('Variable X:'),
                        dcc.Dropdown(className='',id='pie-sensor-x',options=[{'label':'Sound 1', 'value':'Sound 1'},
                                                                             {'label':'Sound 2', 'value':'Sound 2'}],#for x in variables, ##Make it General
                                                        value='Sound 1')]),
    
                    html.Div(className='six columns', children=[              
                        html.Label('Variable Comp:'),
                        dcc.Dropdown(id='pie-sensor-compare',options=[{'label':'Temperature', 'value':'Temperature'},
                                                                      {'label':'Humidity', 'value':'Humidity'},
                                                                      {'label':'Light', 'value':'Light'},
                                                                      {'label':'Sound 1', 'value':'Sound 1'},
                                                                      {'label':'Sound 2', 'value':'Sound 2'}],#for x in variables, ##Make it General
                                                        value='Temperature')]),
                    ]),
            html.Div(className='row', children=[
                    dcc.Graph(id='pie-sensor'),
                    dcc.RangeSlider(id='third-slider',
                                min=0,max=900, step=1, value=[0,900], 
                             )])
            ]),
        html.Div(className='eleven columns',style={'overflow-x':'scroll'}, children=[
            html.H3('User data table',className='third-title'),
            dcc.Slider(id='table-slider',
                       min=0, max=800,step=1,value=0),
            html.Div(id='hist-table'),
           
        ])                                 

            
   ])