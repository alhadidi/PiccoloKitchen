# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:15:45 2020

@author: Alejandro Garcia

Script to create the dashboard about project information. Here it is 
designed the page structure, all callback functions are defined in the main script.

"""

import dash_core_components as dcc
import dash_html_components as html
import dash_gif_component as gif

Project_Overview_layout=html.Div([
        html.H4(className='tab-title',
                children=['Piccolo Kitchen Project Overview']),
        html.Div(className='five columns container',children=[
                html.H6(children=['Brief description: ']),
                html.P(children=['This project aims to create a modular platform for exploring micro-kitchens that are culture specific. Cooking is a personal experience that has cultural attributes. This project explores new modes of cooking using robotically enabled cabinets and appliances to minimize the footprint of the kitchen, while maximizing the ability for users to cook large meals, socialize, and utilize the same space during non-meal times for work. Piccolo kitchen is one of the components of the micro-units that are currently under development as part of the CityHome 02 projects.'],
                style={'margin':'20px'})
                ]),
        html.Div(className='six columns',children=[
                gif.GifPlayer(
                        gif='../assets/Kitchen+Unit.gif',
                        still='../assets/Kitchen+Unit.jpg',
#                        autoplay=False
                                        )
                
                
                ])
                
                
                
                ])