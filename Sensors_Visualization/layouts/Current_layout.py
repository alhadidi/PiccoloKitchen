# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:50 2019

@author: Alejandro Garcia

Script to create the dashboard about actual status of the kitchen user. Here it is 
designed the page structure, all callback functions are defined in the main script.


"""


import dash_core_components as dcc
import dash_html_components as html


Current_layout=html.Div([
                        html.H5(className='tab-title',
                                children=['Current Kitchen Status']),
                        html.Div(className='row',children=[
                            html.Div(className='five columns',children=[
    
                                    dcc.Interval(id='intervals-pos',
    #                                             interval=0.1*1000, # in milliseconds USEFULL FOR REAL
                                                 interval=1*1000,
                                                 n_intervals=0),
                                    html.Div(className='', children=[
                                            html.H5('User Position'),
                                            dcc.Slider(className='eight columns',
                                                       id='pos-slider',
                                                       min=0,max=400,
                                                       step=1,
                                                       value=0),
                                            dcc.Graph(id='user-pos')
                                    ]),
                                    html.Br(),
                                    html.Div(className='row', children=[
                                        html.Div(className='small-title',children=[
                                                html.H5(className='six columns small-title',children=[
                                                        'Front Cabinet']),
                                                html.H5(className='six columns small-title',children=
                                                         "Up")       
                                            ]),
                                        html.Div(className='',children=[
                                                html.H5(className='six columns small-title',children=[
                                                        'Back Cabinet']),
                                                html.H5(className='six columns small-title',children=
                                                         "High")       
                                           ])
                                    ])
                            ]),
                            html.Div(className='seven columns',children=[
    
                                    dcc.Interval(id='intervals-ter',
    #                                             interval=0.1*1000, # in milliseconds USEFULL FOR REAL
                                                 interval=1*1000,
                                                 n_intervals=0),
                                    html.Div(className='', children=[
                                            html.H5('Enviroment Data'),
                                            dcc.Graph(id='real-ter')
                                    ]),
    
                                ]),
                        ]),
])