# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:09:10 2019

@author: Alejandro
"""

from datetime import datetime
import dash
from statistics import mean
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import plotly.subplots as subplots
import pandas as pd
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors ={
        'background':'rgb(0,0,0)',
        'text': '#eeeeee',
        'title': '#eeeeee',
        'right': 'rgba(128, 128, 128, 0.2)',
        'kitchen_top': 'rgba(128, 128, 128, 0.5)',
        'led':'rgba(128, 128, 128, 0.1)'
        }

app.layout=html.Div(style={'backgroundColor':colors['background']},children=[
        html.Div(style={'padding':20}),
        html.H1(children=dcc.Markdown('**Piccolo Kitchen**'), style={'fontSize':75,'color': colors['title'], 'textAlign':'center'}),
        html.Div(style={'padding':5}),
        html.H2(children=dcc.Markdown('Project developed by MIT Media Lab - [City Science](https://www.media.mit.edu/groups/city-science/overview/)'),
                 style={'color':colors['text'], 'textAlign':'center','fontSize':45}),
        html.Div(style={'padding':15}),
        html.Div([
            html.Div([           
                   html.H3(dcc.Markdown('**TerMITes Enviromental real time data**'),style={'textAlign':'left','fontSize':35,'backgroundColor':colors['right'],'padding':'10px 10px 10px 10px'}),
                   dcc.Graph(id='termite'),
    
                   dcc.Interval(
                        id='interval-component',
                        interval=1*1000, # in milliseconds
                        n_intervals=0
                        )
                   ],style={}),
                             
    
                   #Right Side
                   html.Div(style={'padding':1}),
                   html.Div(
                       html.H3([
                           dcc.Markdown('**Kitchen Status**'),
                           html.H4(id='time',style={'fontSize':35,'paading':5,'textAlign':'center','fontWeight':'bold'}),
                           html.Button('Refresh', id='refresh',
                                       style={'backgroundColor':'white',
                                              'width':190,
                                              'heigt':70,
                                              'fontSize':20,
                                              'padding':'0px 0px 0px 0px'})]

                           ,style={'borderColor':'white','backgroundColor':colors['right'],'color':colors['text'],
                                   'fontSize':35,'columnCount':3,'padding':'10px 10px 10px 10px'})
                       ),       
#                   html.Div(style={'padding':10,'backgroundColor':'black'}),
                   dcc.Interval(
                        id='interval-numbers',
                        interval=20*1000, # in milliseconds
                        n_intervals=0
                        ),
                   html.Div(style={'columnCount':3}, children=[
                           html.Div(style={'backgroundColor': colors['kitchen_top']}, children=[
                                    html.H3(dcc.Markdown('**Kitchen Top**'),style={'padding':10}),
                                    html.H4(dcc.Markdown('Temperature *(ºC)*'),
                                           style={'padding':'0px 0px 0px 0px'}),
                                    daq.LEDDisplay(
                                      id='Temp_G',
                                      value="00.00",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      style={'padding':'20px 0px 50px 60px'}
                                    ) , 
                                    html.H4(dcc.Markdown('Humidity *(%)*')),
                                    daq.LEDDisplay(
                                      id='Hum_G',
                                      value="34.16",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      style={'padding':'20px 0px 50px 60px'}
                                    ) ,                                 
                                    html.H4(dcc.Markdown('Light *(Lux)*')),
                                    daq.LEDDisplay(
                                      id='Lit_G',
                                      value="234.82",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      style={'padding':'20px 0px 50px 60px'}
                                    ) ,   
                                    html.Div(style={'padding':114}),
                           ]),
                           html.Div(style={'padding':2}),
                           html.Div(style={'backgroundColor':colors['right']}, children=[
                                    html.H3(dcc.Markdown('**Front Cabinet**'),style={'padding':'10px 5px 5px 0px'}),
                                    html.H4('Temperature'),
                                    daq.LEDDisplay(
                                      id='Temp_F',
                                      value="234.82",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      style={'padding':'20px 0px 50px 60px',
                                             'borderColor':colors['led']}
                                    ) ,                                 
                                    html.H4('Humidity'),
                                    daq.LEDDisplay(
                                      id='Hum_F',
                                      value="234.82",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      theme='Dark',
                                      style={'padding':'20px 0px 50px 60px',
                                              'borderColor':colors['led']}
                                    ) ,                                 
                                    html.H4 ('Position'),
                                    html.Div(style={'padding':10}),
                                    html.Div(style={'columnCount':2},children=[
                                    html.Div('- Up: ',style={'padding':'1px 0px 0px 60px','fontSize':20}),         
                                    daq.Indicator(
                                      id='front-led-up',
                                      value=True,
#                                      color="green",
                                      style={'padding':'35px 0px 20px 10px',
                                              'borderColor':colors['led']},
                                      size=30
                                        )  ]),
                                    html.Div(style={'columnCount':2},children=[
                                    html.Div('- Down: ',style={'padding':'10px 0px 0px 60px','fontSize':20}),         
                                    daq.Indicator(
                                      id='front-led-down',
                                      value=True,
    #                                  color="red",
                                      style={'padding':'30px 0px 20px 10px',
                                              'borderColor':colors['led']},
                                      size=30
                                    )  ]),
                                    html.Div(style={'columnCount':2},children=[
                                            html.Div(dcc.Markdown('**Number of interactions:** '),style={'padding':'1px 0px 0px 10px','fontSize':20}),         
                                            html.Div(id='number-front',children=-1,style={'fontSize':30,
                                                                                          'padding':'10px 0px 0px 20px'})]),
                                    html.Div(style={'padding':89}),
                                                       ]),
                           html.Div(style={'padding':1}),
                           html.Div(style={'backgroundColor':colors['right']}, children=[
                                    html.H3(dcc.Markdown('**Back Cabinet**'),style={'padding':'10px 0px 5px 0px'}),
                                    html.H4('Temperature'),
                                    daq.LEDDisplay(
                                      id='Temp_B',
                                      value="234.82",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      style={'padding':'20px 0px 50px 60px'}
                                    ) ,                                 
                                    html.H4('Humidity'),
                                    daq.LEDDisplay(
                                      id='Hum_B',
                                      value="234.82",
                                      backgroundColor=colors['led'],
                                      size=40,
                                      style={'padding':'20px 0px 50px 60px'}
                                    ) ,                                 
                                    html.H4 ('Position'),
                                    html.Div(style={'padding':10}),
                                    html.Div(style={'columnCount':2},children=[
                                    html.Div('- Up: ',style={'padding':'1px 0px 0px 60px','fontSize':20}),         
                                    daq.Indicator(
                                      id='back-led-up',
                                      value=True,
#                                      color="red",
                                      style={'padding':'35px 0px 20px 10px',
                                              'borderColor':colors['led']},
                                      size=30
                                        )  ]),
                                    html.Div(style={'columnCount':2},children=[
                                    html.Div('- Down: ',style={'padding':'10px 0px 0px 60px','fontSize':20}),         
                                    daq.Indicator(
                                      id='back-led-down',
                                      value=True,
#                                      color="red",
                                      style={'padding':'30px 0px 20px 10px',
                                              'borderColor':colors['led']},
                                      size=30
                                    )  ]),
                                    html.Div(style={'columnCount':2},children=[
                                            html.Div(dcc.Markdown('**Number of interactions:** '),style={'padding':'1px 0px 0px 10px','fontSize':20}),         
                                            html.Div(id='number-back',children=-1,style={'fontSize':30,
                                                                                          'padding':'10px 0px 0px 20px'})]),
                                    html.Div(style={'padding':90}),
                            ])                
                                                  
                         ] ),
    #               dcc.Interval(
    #                    id='interval-table',
    #                    interval=1*100000, # in milliseconds
    #                    n_intervals=0
    #                    ),
    #               html.Div(id='Table_Ter'),
                
                    ],
                    #'width': '49%',
                style={'color':colors['text'],'display': 'inline-block','padding': '0px 20px 20px 20px','columnCount':2})                  

            
        
   
            
             
                
])
@app.callback(
        Output('termite', 'figure'),
        [Input('interval-component', 'n_intervals')])
def update_graph_t(n):
        liv_ter=pd.read_csv('C:/Users/Alejandro/Desktop/MIT Media Lab/codes/terMITes/csv_serial.csv') 

        trace_t=go.Scatter(                         
                      y= liv_ter.iloc[-200:,4].tolist(),
                      line={'color':'red'},
                      fill='tozeroy',
                      fillcolor='rgba(255,102,102,0.1)',
                      mode='lines+text'
                     )
        trace_h=go.Scatter(             
                      y= liv_ter.iloc[-200:,6].tolist(),
                      line={'color':'blue'},
                      fill='tozeroy',
                      fillcolor='rgba(153,153,255,0.1)',
#                      mode='lines+markers'
                     )
        trace_l=go.Scatter(             
                      y= liv_ter.iloc[-200:,5].tolist(),
                      line={'color':'yellow'},
                      fill='tozeroy',
                      fillcolor='rgba(230,255,0,0.1)'
                     )

        fig = subplots.make_subplots(rows=3, cols=1, specs=[[{}], [{}], [{}]],
                                  shared_xaxes=True, shared_yaxes=True,
                                  vertical_spacing=0.05,subplot_titles=('Temperature','Humidity','Light'))
        fig.append_trace(trace_t, 1, 1)
        fig.append_trace(trace_h, 2, 1)
        fig.append_trace(trace_l, 3, 1)
        
        fig['layout'].update(height=936, width=1100, title='Termites',plot_bgcolor=colors['background'],
                            paper_bgcolor=colors['background'], showlegend=False,
                            xaxis={'gridcolor':'dimgrey','showgrid':True},
                            yaxis={'range':[26,31],'title': 'ºC','gridcolor':'dimgrey','showgrid':True},
                            xaxis2={'gridcolor':'dimgrey','showgrid':True},
                            yaxis2={'range':[29.5,31.5],'title':'%','gridcolor':'dimgrey','showgrid':True},
                            xaxis3={'gridcolor':'dimgrey','showgrid':True},
                            yaxis3={'range':[250,700],'title':'Lux','gridcolor':'dimgrey','showgrid':True},
                            font={'color':colors['text']})
        return  fig
@app.callback(
        [Output('time','children'),
         Output('Temp_G', 'value'),
         Output('Hum_G', 'value'),
         Output('Lit_G', 'value'),
         Output('Temp_F', 'value'),
         Output('Hum_F', 'value'),
         Output('front-led-up', 'color'),
         Output('front-led-down', 'color'),
         Output('Temp_B', 'value'),
         Output('Hum_B', 'value'),
         Output('back-led-down', 'color'),
         Output('back-led-up', 'color'),
         Output('number-front', 'children'),
         Output('number-back', 'children')
         ],
        [Input('interval-numbers', 'n_intervals')]
        ,[State('front-led-up', 'color'),
         State('back-led-up', 'color'),
         State('number-front', 'children'),
         State('number-back', 'children')]
        )
def udpate_g(n_clicks,color_f,color_b,n_front,n_back):
    time=datetime.now().strftime('%H:%M:%S')
    udp_t=pd.read_csv('C:/Users/Alejandro/Desktop/MIT Media Lab/codes/terMITes/csv_udp.csv') 
    temp_g=str(round(mean(udp_t.iloc[-600:,6]),2)-4)
    hum_g=str(round(mean(udp_t.iloc[-600:,7]),2))
    lit_g=str(round(mean(udp_t.iloc[-600:,8]),1))
    temp_f=str(round(mean(udp_t.iloc[-600:,3]),2)-2)
    hum_f=str(round(mean(udp_t.iloc[-600:,4]),2))
    pos_f=(udp_t.get_value(-1,5,takeable=True)) 
    temp_b=str(round(mean(udp_t.iloc[-600:,0]),2)-2)
    hum_b=str(round(mean(udp_t.iloc[-600:,1]),2))
    pos_b=((udp_t.get_value(-1,2,takeable=True)))
    if (pos_b=='Up'):
        color_bu='green'
        color_bd='red'
    elif (pos_b=='Down'):
        color_bu='red'
        color_bd='green'
    else:
        color_bu='red'
        color_bd='red'
    if (pos_f=='Up'):
        color_fu='green'
        color_fd='red'
    else:
        color_fu='red'
        color_fd='green'
    if (color_f!=color_fu):
        n_front+=1
    else:
        n_front=n_front
    if (color_b!=color_bu):
        n_back+=1
    else:
        n_back=n_back

    

    return time,temp_g,hum_g,lit_g,temp_f,hum_f,color_fu,color_fd,temp_b,hum_b,color_bd,color_bu,n_front,n_back
   
#@app.callback(
#        Output('number-front','children'),
#        [Input('front-led-up','color')],
#        [State('number-front','children'),State('front-led-up','color')])
#def update_front_n(n,value,color):
#    value+=1
#    return value
#@app.callback(
#        Output('number-back','children'),
#        [Input('back-led-up','color')],
#        [State('number-back','children')])
#def update_back_n(color,value):
#    value+=1
#    return value

if __name__ == '__main__':
    app.run_server(debug=False)