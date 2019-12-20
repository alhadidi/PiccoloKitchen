# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:18:36 2019

@author: Alejandro Garcia
Script for the design of the header in the visual tool
"""

import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header=html.Div(
                html.Div(id='title',className='row',children=[
                        html.H5(['Piccolo Kitchen Data Visualisation'],
                               className='ten columns main-title',
                               ),
                        html.Img(className='one columns',
                            src=app.get_asset_url("cs_logo.png"),
                            id="cs-logo",
    #                        style={"height": "90px", "width": "auto",
    #                            "margin-bottom":"25px","margin-right":"10px",
    #                       }
                        ),
                        html.Img(className='one columns',
                            src=app.get_asset_url("media_logo.png"),
                            id="media-logo",
    #                        style={"height": "90px", "width": "auto",
    #                            "margin-bottom": "25px","margin-right":"10px",
    #                       }
                        ),
                    ]),                                               
                html.Div(id='SubHeader',className='row',children=[
                        html.H2(className='twelve columns main-subtitle',children=dcc.Markdown('Project developed by MIT Media Lab - [City Science](https://www.media.mit.edu/groups/city-science/overview/)')),
                       ])
        )
    return header

def get_menu():
    menu=html.Div(
            [
                dcc.Link(
                    "Project Information",
                    href="/dash-financial-report/overview",
                    className="tab first",
                ),
                dcc.Link(
                    "Enviromental measures",
                    href="/dash-financial-report/price-performance",
                    className="tab",
                ),
                dcc.Link(
                    "User-Kitchen Interaction",
                    href="/dash-financial-report/portfolio-management",
                    className="tab",
                ),
                dcc.Link(
                    "User behavior", href="/dash-financial-report/fees", className="tab"
                ),
                dcc.Link(
                    "Overall Analysis",
                    href="/dash-financial-report/distributions",
                    className="tab",
                ),
                dcc.Link(
                    "Comments",
                    href="/dash-financial-report/news-and-reviews",
                    className="tab",
                ),
            ],
            className="row all-tabs",
        )
    return menu