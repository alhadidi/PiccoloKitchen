# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:47:20 2019
This script  will be the visual tool for the first Piccolo Kitchen Sensors.

Using plotly Dash tool and an underdevelopment CSS for different components.
On the next step we will include React components created for thi project.


@author: Alejandro Garcia

"""

""" Import libraries,files and Serial, UDP connections"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.subplots as subplots
import pandas as pd
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import socket
import random
import sys
sys.path.append('layouts/')

from header_extra import Header
from Project_Overview_layout import Project_Overview_layout
#from termites_visual import terMITes_layout
from Sensors_layout import Sensors_layout
from Current_layout import Current_layout
from Enviromental import Enviromental_layout
from Storage_layout import Storage_layout


pio.templates.default = "plotly_dark" 

#   IF USING SERIAL OR UDP COMUNICATOIN 

#ser = serial.Serial(
#    port='COM4',\
#    baudrate=9600,\
#    parity=serial.PARITY_NONE,\
#    stopbits=serial.STOPBITS_ONE,\
#    bytesize=serial.EIGHTBITS,\
#    )
########MODIFY THE FOLLOWING TWO LINES ##########################################################
#UDP_IP = "192.168.43.156" #Use the same address that was specified on the UDP Settings.
#UDP_PORT = 19900 #Use the same port that was specified on the UDP Settings.
#################################################################################################
#
#sock = socket.socket(socket.AF_INET, # Internet
#                     socket.SOCK_DGRAM) # UDP
#sock.bind((UDP_IP, UDP_PORT))

""" CSS Styles Included in the design"""
#external_stylesheets = ['https://codepen.io/agarciag/pen/ZEEmeWr.css', #General CSS
#                        'https://codepen.io/agarciag/pen/WNvZbOo.css'] #Particular CSS
# --------------------------------------------------------------------------------------
""" File read and data preparation """
file_name='kitchen_status.csv'
#file_pos='C:/Users/Alejandro/Desktop/MIT Media Lab/PiccoloKitchen/codes/Git/HomeData-Visuals/Data/user_position.csv'
data=pd.read_csv(file_name)
data=data.round(2)
data_tras=data.set_index('Time').T

#user_pos=pd.read_csv(file_pos)
liv_ter=pd.read_csv('csv_serial.csv') 
variables=data.columns
variables_time=data.set_index('Time').columns
# --------------------------------------------------------------------------------------
""" Dash tool """

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
colors ={
        'background':'black',
        'text': 'white',
        'title': 'lightgrey',
        'right': 'rgba(128, 128, 128, 0.2)',
        'kitchen_top': 'rgba(128, 128, 128, 0.5)',
        'led':'rgba(128, 128, 128, 0.1)'
        }

server=app.server
app.title="Home Data Dashboard"
app.layout=html.Div(children= [       
        html.Div(id='title',className='row',children=[
                html.Div([
                        html.H5(['Piccolo Kitchen Data Visualization'],
                               className='seven columns main-title',
                               ),
                        html.H5(className='five columns main-subtitle',
                                children=dcc.Markdown('Project developed by MIT Media Lab - [City Science](https://www.media.mit.edu/groups/city-science/overview/)')),    
                        ]),                              
                ]),
        html.Div(
            [
                dcc.Interval(id='intervals-layouts',
    #                                             interval=0.1*1000, # in milliseconds USEFULL FOR REAL
                    interval=1*1000,
                    n_intervals=0),
                dcc.Link(
                    "Project Overview",
                    href="/kitchen-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    "Environment", href="/kitchen-report/EnvironmentData",
                    className="tab"
                ),
#                dcc.Link(
#                    "TerMITes",
#                    href="/dash-kitchen-report/terMITes",
#                    className="tab",
#                ),
                dcc.Link(
                    "Historical Data Visualisation",
                    href="/kitchen-report/HistoricData",
                    className="tab",
                ),

                dcc.Link(
                    "Storage Status",
                    href="/kitchen-report/StorageData",
                    className="tab",
                ),
#                dcc.Link(
#                    "Comments",
#                    href="/dash-financial-report/news-and-reviews",
#                    className="tab",
#                ),
            ],
            className="row all-tabs",
        ),
            dcc.Location(id='url',refresh=False),

        html.Div(id='hidden-div', style={'display':'none'}),
        html.Div(className='row',id='central-page'),              
                  
])


Development_layout=html.Div([
                            html.H5(className='development-title',
                                    children=['Page under development.']),
                            
                        ])

# --------------------------------------------------------------------------------------
""" Callback functions included in the Dashboard """
    
@app.callback(
        Output('main-graph','figure'),
        [Input('var-dropdown','value'),
         Input('first-slider','value')])

def data_graph(variable,value_s):
    first_graph={
    'data':[go.Scatter(                         
              y= data.loc[:,variable].tolist(),
              x=data.iloc[:,0].tolist(),
              line={'color':'rgb(133, 196, 201)'},
#              fill='tozeroy',
#              fillcolor='lightblue',
             )],
     'layout': {
             'yaxis':{'fixedrange':False,
#                      'range':[20,33],
                      'tickfont':{'size':14},
                      'gridcolor':'black',
                      'title':variable},
             'xaxis':{'nticks':7,
                      'tickangle':30,
                      'tickfont':{'size':14},
                      'gridcolor':'black'},
             'title': {'text':variable,
                       'x':0.1,
                       },
             'plot_bgcolor':'black',
             'paper_bgcolor':'black',
             'font': {  'size':15,
                        'color': 'white'},
             'height':500,
                }
}
#    figure=px.line(data,x='Time',y=variable,title='User Interaction',range_x=value_s,color_discrete_sequence=px.colors.diverging.Tealrose)
    return  first_graph
                        
@app.callback(
        Output('bar-sensor','figure'),
        [Input('bar-sensor-x','value'),
         Input('bar-sensor-compare','value')])
def user_bar_graph(value_x,value_c):
    figure=px.histogram(data,x=value_x ,color=value_c,title='Position Study',color_discrete_sequence=px.colors.diverging.Tealrose)#,marginal='rug')
    figure.update_layout({'legend_orientation':'h'})
    return figure

@app.callback(
        Output('pie-sensor','figure'),
        [Input('pie-sensor-x','value'),
         Input('pie-sensor-compare','value'),
         Input('third-slider','value')])
def user_bar_graph(value_y,value_c,value_s):
    figure=px.scatter_3d(data,x='Time',y=value_y ,z=value_c,color='Light',title='Environmental Data',range_x=value_s,color_continuous_scale=px.colors.diverging.Tealrose)#,marginal='rug')
    figure.update_layout({'legend_orientation':'h'})
    return figure

@app.callback(
        Output('user-pos','figure'),
        [Input('intervals-pos','n_intervals')]
#        [Input('pos-slider','value')]
        )
def update_user_pos(n_intervals):
    data_y=500
    data_x=500
# ***IF USING SERIAL READ***
#    data=(ser.readline().decode('utf-8'))
#    print(data)
    
#    data=pd.DataFrame([[data_x,data_y]],columns=['x','y'])
#    try:
##        data_x=data.split('/')[0]
##        data_y=data.split('/')[1].strip('\r\n')
##        data=pd.DataFrame([[data_x,data_y]],columns=['x','y'])
#    except:
#        data_y=500
#        data_x=500
##        data=pd.DataFrame([[data_x,data_y]],columns=['x','y'])
##        print(data_y)
##    figure=px.scatter(data,x='x',y='y')
    return  {
            'data':[go.Scatter(x=[float(user_pos.iloc[n_intervals,0])],y=[float(user_pos.iloc[n_intervals,1])],marker_size=15,marker_color='#ff0000'),
#                    go.Scatter(x=[float(user_pos.iloc[n_intervals+3,0])],y=[float(user_pos.iloc[n_intervals+3,1])],marker_size=15,marker_color='#ff8080'),
#                    go.Scatter(x=[float(user_pos.iloc[n_intervals+6,0])],y=[float(user_pos.iloc[n_intervals+6,1])],marker_size=15,marker_color='#ff4d4d'),
#                    go.Scatter(x=[float(user_pos.iloc[n_intervals+9,0])],y=[float(user_pos.iloc[n_intervals+9,1])],marker_size=15,marker_color='#ff0000')
                    ],
#           'data':[go.Scatter(x=[data_x],y=[data_y],marker_size=20)],
            'layout':{'paper_bgcolor':colors['background'],
                      'plot_bgcolor':colors['background'],
                      'marker': {'size': 40},
                      'height':500,
                      'width':600,
                      'xaxis':{'title':data_x,'range':[0,1200],'zeroline':False,'gridcolor':'grey'},
                      'yaxis':{'title': data_y,'range':[0,1000],'zeroline':False,'gridcolor':'grey'}                                                     
                      }
              }    

@app.callback(
        Output('real-ter','figure'),
        [Input('intervals-ter','n_intervals')]
#        [Input('pos-slider','value')]
        )
def update_real_ter(n_intervals):
#    **IF CONNECTING TERMITA VIA UDP**
#        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#    
#        temp=data.decode().replace(' = ',':').split(' ')[4].split(':')[1]
#        hum=data.decode().replace(' = ',':').split(' ')[6].split(':')[1]
#        lit=data.decode().replace(' = ',':').split(' ')[5].split(':')[1]
        
        trace_t=go.Scatter(                         
                      y= liv_ter.iloc[-1000:,4].tolist(),
                      line={'color':'red'},
                      fill='tozeroy',
                      fillcolor='rgba(255,102,102,0.1)',
                     
                     )
        trace_h=go.Scatter(             
                      y= liv_ter.iloc[-1000:,6].tolist(),
                      line={'color':'blue'},
                      fill='tozeroy',
                      fillcolor='rgba(153,153,255,0.1)',
#                      mode='lines+markers'
                     )
        trace_l=go.Scatter(             
                      y= liv_ter.iloc[-1000:,5].tolist(),
                      line={'color':'yellow'},
                      fill='tozeroy',
                      fillcolor='rgba(230,255,0,0.1)'
                     )

        fig = subplots.make_subplots(rows=3, cols=1, specs=[[{}], [{}], [{}]],
                                  shared_xaxes=True, shared_yaxes=True,
                                  vertical_spacing=0.1,subplot_titles=('Temperature','Humidity','Light'))
        fig.append_trace(trace_t, 1, 1)
        fig.append_trace(trace_h, 2, 1)
        fig.append_trace(trace_l, 3, 1)
        
        fig['layout'].update(height=800,plot_bgcolor=colors['background'],
                            paper_bgcolor=colors['background'], showlegend=False,
                            xaxis={'gridcolor':'dimgrey','showgrid':True},
                            yaxis={'range':[27,31],
                                   'title': 'ºC','gridcolor':'dimgrey','showgrid':True},
                            xaxis2={'gridcolor':'dimgrey','showgrid':True},
                            yaxis2={'range':[29,30],
                                    'title':'%','gridcolor':'dimgrey','showgrid':True},
                            xaxis3={'gridcolor':'dimgrey','showgrid':True},
                            yaxis3={'range':[500,600],
                                    'title':'Lux','gridcolor':'dimgrey','showgrid':True},
                            font={'color':colors['text'],'size':17})
        return  fig
def generate_table_user(dataframe,variables):
    return html.Table(
        # Header
      
        [html.Tr([html.Th(col) for col in dataframe.columns])] + 
        # Body  
        [html.Tr([html.Td(dataframe.loc[i][col]) for col in dataframe.columns]) for i in variables]
    )
variables_table=['Position','Position Back','Position Front R','Position Front L','Temperature','Humidity','Light']

@app.callback(
        Output('hist-table','children'),
        [Input('table-slider','value')])
def display_table(value):
    data_table=data_tras.iloc[:,value:value+50:5]
    data_table.insert(0,'Variables \ Time',variables_time,True)
    return generate_table_user(data_table,variables_table)
            
# --------------------------------------------------------------------------------------
""" Data upload functions """

#@app.callback(
#        Output('hist-table','children'),
#        [Input('table-slider','value')])
#def update_data(filename):
#    
#    return data


# --------------------------------------------------------------------------------------
""" Callback function which includes all different layouts """      
  
@app.callback(
        Output('central-page','children'),
        [Input('url','pathname')]
        )
def display_page(pathname):
    if pathname=="/kitchen-report/overview":
        return(Project_Overview_layout
               )
    elif pathname=="/kitchen-report/EnvironmentData":
        return(Enviromental_layout
               )
    elif (pathname=="/kitchen-report/HistoricData"):
        return (Sensors_layout               
                )
    elif (pathname=="/kitchen-report/StorageData"):
        return (Storage_layout               
                )
    else:
        return(Sensors_layout             
               )                        


                   
#Main
if __name__ == "__main__":
    app.run_server(debug=True)
