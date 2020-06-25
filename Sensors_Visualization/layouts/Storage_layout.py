# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:50 2019

@author: Alejandro Garcia

Script to create the dashboard about actual status of the kitchen user. Here it is 
designed the page structure, all callback functions are defined in the main script.


"""


import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
colors ={
        'background':'rgb(0,0,0)',
        'text': '#eeeeee',
        'title': '#eeeeee',
        'right': 'rgba(128, 128, 128, 0.2)',
        'kitchen_top': 'rgba(128, 128, 128, 0.5)',
        'led':'rgba(128, 128, 128, 0.1)'
        }

Storage_layout=html.Div([
                       
                        html.Div(className='row',children=[
                            
                            html.Div(className='five columns',children=[
                                    html.H4(className='tab-title',
                                           children=['Storage Kitchen Status']),
                                    html.Div(className='pretty-container row eleven columns',children=[
                                           html.H4('Back Cabinet'),
                                           html.Div(className='row eleven columns',children=[
                                                   html.Div(className='four columns',children=[
                                                          html.H6(dcc.Markdown('Temperature *(ºC)*')),
                                                           daq.LEDDisplay(
                                                              id='Temp_G',
                                                              value="24.30",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),
                                                   html.Div(className='four columns',children=[
                                                           html.H6(dcc.Markdown('Humidity *(%)*')),
                                                           daq.LEDDisplay(
                                                              id='Temp_G',
                                                              value="32.10",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),
                                                   html.Div(className='four columns',children=[
                                                           html.H6(dcc.Markdown('Light *(Lux)*')),
                                                           daq.LEDDisplay(                                                            
                                                              id='Temp_G',
                                                              value="154.30",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),     
                                                   ]),
                                           html.Br(),
                                           html.Div(className='row eleven columns',children=[
                                                         html.H6(className='three columns small-title',children=[
                                                        'Position:']),
                                                         html.Div(className='three columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=False,
                                                                      color="red",
                                                                      style={'padding':'18px 0 0 0',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="High")]),
                                                         html.Div(className='three columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=True,
                                                                      color="green",
                                                                      style={'padding':'18px 0 0 0',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="Med")]),
                                                         html.Div(className='three columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=True,
                                                                      color="red",
                                                                      style={'padding':'18px 0px 0px 0px',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="Low")]),
                                                         html.H6(className='six columns',children=[
                                                        'Number of Interactions']),
                                                         html.H6(className='four columns',children=
                                                         "7")  
                                                   ]),
                                            ]),
                                    
                                    html.Div(className='pretty-container row eleven columns',children=[
                                           html.H4('Right Front Cabinet'),
                                           html.Div(className='row eleven columns',children=[
                                                   html.Div(className='four columns',children=[
                                                          html.H6(dcc.Markdown('Temperature *(ºC)*')),
                                                           daq.LEDDisplay(
                                                              id='Temp_G',
                                                              value="23.12",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),
                                                   html.Div(className='four columns',children=[
                                                           html.H6(dcc.Markdown('Humidity *(%)*')),
                                                           daq.LEDDisplay(
                                                              id='Temp_G',
                                                              value="45.3",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),
                                                   html.Div(className='four columns',children=[
                                                           html.H6(dcc.Markdown('Light *(Lux)*')),
                                                           daq.LEDDisplay(                                                            
                                                              id='Temp_G',
                                                              value="10.00",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),     
                                                   ]),
                                           html.Br(),
                                           html.Div(className='row eleven columns',children=[
                                                         html.H6(className='three columns small-title',children=[
                                                        'Position:']),
                                                         html.Div(className='four columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=False,
                                                                      color="red",
                                                                      style={'padding':'18px 0 0 0',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="Up")]),
                                                         html.Div(className='four columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=True,
                                                                      color="green",
                                                                      style={'padding':'18px 0 0 0',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="Down")]),

                                                         html.H6(className='six columns',children=[
                                                        'Number of Interactions']),
                                                         html.H6(className='four columns',children=
                                                         "3"),]),
                                    ]),                              
                                    html.Div(className='pretty-container row eleven columns',children=[
                                           html.H4('Left Front Cabinet'),
                                           html.Div(className='row eleven columns',children=[
                                                   html.Div(className='four columns',children=[
                                                          html.H6(dcc.Markdown('Temperature *(ºC)*')),
                                                           daq.LEDDisplay(
                                                              id='Temp_G',
                                                              value="32.45",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),
                                                   html.Div(className='four columns',children=[
                                                           html.H6(dcc.Markdown('Humidity *(%)*')),
                                                           daq.LEDDisplay(
                                                              id='Temp_G',
                                                              value="28.30",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),
                                                   html.Div(className='four columns',children=[
                                                           html.H6(dcc.Markdown('Light *(Lux)*')),
                                                           daq.LEDDisplay(                                                            
                                                              id='Temp_G',
                                                              value="543.39",
                                                              backgroundColor=colors['led'],
                                                              size=20,
    #                                                          style={'padding':'20px 0px 50px 60px'}
                                                               )]),     
                                                   ]),
                                           html.Br(),
                                           html.Div(className='row eleven columns',children=[
                                                         html.H6(className='three columns small-title',children=[
                                                        'Position:']),
                                                         html.Div(className='four columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=False,
                                                                      color="green",
                                                                      style={'padding':'18px 0 0 0',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="Up")]),
                                                         html.Div(className='four columns',children=[
                                                                 daq.Indicator(
                                                                      id='front-led-down',
                                                                      className='three columns',
                                                                      value=True,
                                                                      color="red",
                                                                      style={'padding':'18px 0 0 0',
                                                                              'borderColor':colors['led']},
                                                                      size=10
                                                                    ),
                                                                 html.H6(className='nine columns', children="Down")]),

                                                         html.H6(className='six columns',children=[
                                                        'Number of Interactions']),
                                                         html.H6(className='four columns',children=
                                                         "2")
                                                         ]),

                                            ]),
                                    ]),
                            html.Div(className='seven columns',children=[
                                    html.Br(),
                                    html.Br(),
                                    dcc.Interval(id='intervals-ter',
    #                                             interval=0.1*1000, # in milliseconds USEFULL FOR REAL
                                                 interval=1*1000,
                                                 n_intervals=0),
                                    html.Div(className='', children=[
                                            html.H5('Kitchen Cooktop Status'),
                                            dcc.Graph(id='real-ter')
                                    ]),
    
                                ]),
                        ]),
])