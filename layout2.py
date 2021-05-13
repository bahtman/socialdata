import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px


from app import app
from filtering import *

temp = list(map(int,[full_df['Temperature'].quantile(0.005),full_df['Temperature'].quantile(0.995)]))
hum = list(map(int,[full_df['Humidity'].min(),full_df['Humidity'].quantile(0.995)]))
vis = list(map(int,[full_df['Visibility'].min(),full_df['Visibility'].quantile(0.995)]))
wind = list(map(int,[full_df['Wind_Speed'].min(),full_df['Wind_Speed'].quantile(0.995)]))

control = dbc.Row([
    dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Temperature"),
                dcc.RangeSlider(
                    id = 'temp',
                    min=temp[0],
                    max=temp[1],
                    marks={
                        temp[0]: {'label': f'{temp[0]}°C', 'style': {'color': '#77b0b1'}},
                        temp[1]: {'label': f'{temp[1]}°C', 'style': {'color': '#f50'}}
                    },
                    value=temp
                ),  
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Humidity"),
                dcc.RangeSlider(
                    id = 'hum',
                    min=hum[0],
                    max=hum[1],
                    marks={
                        hum[0]: {'label': f'{hum[0]}', 'style': {'color': '#77b0b1'}},
                        hum[1]: {'label': f'{hum[1]}', 'style': {'color': '#f50'}}
                    },
                    value=hum
                ),
            ]
        ),
    ],
    body=True,
),
dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Visibility"),
                dcc.RangeSlider(
                    id = 'vis',
                    min=vis[0],
                    max=vis[1],
                    marks={
                        vis[0]: {'label': f'{vis[0]}', 'style': {'color': '#77b0b1'}},
                        vis[1]: {'label': f'{vis[1]}', 'style': {'color': '#f50'}}
                    },
                    value = vis
                ),  
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Wind Speed"),
                dcc.RangeSlider(
                    id = 'wind',
                    min=wind[0],
                    max=wind[1],
                    marks={
                        wind[0]: {'label': f'{wind[0]}', 'style': {'color': '#77b0b1'}},
                        wind[1]: {'label': f'{wind[1]}', 'style': {'color': '#f50'}}
                    },
                    value=wind

                ),
            ]
        ),
    ],
    body=True,
),
],
align="center",
)

kpis = dbc.Card(
    [
dbc.CardBody(
    [
        html.P(
            id='mean_sev'
        )
    ]
),dbc.CardBody(
    [
        html.P(
            id='num_acc'
        )
    ]
),
    ]
)

USmap = html.Div(
        [
            html.Iframe(
                id='Accident_map',
                srcDoc=open('Maps/Accidentmap.html', "r").read(),
                width="100%",
                height="500 px",
            ),
        ],)


main = dbc.Container(
    [
        html.H1("US accidents"),
        html.Hr(),
        control,
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='sev'), md=6),
                dbc.Col(dcc.Graph(id='states'), md=6)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(USmap, md=8),
                dbc.Col(kpis, md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)