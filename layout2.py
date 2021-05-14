import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px


from filtering import *

temp = list(map(int,[full_df['Temperature'].quantile(0.005),full_df['Temperature'].quantile(0.995)]))
hum = list(map(int,[full_df['Humidity'].min(),full_df['Humidity'].quantile(0.995)]))
vis = list(map(int,[full_df['Visibility'].min(),full_df['Visibility'].quantile(0.995)]))
wind = list(map(int,[full_df['Wind_Speed'].min(),full_df['Wind_Speed'].quantile(0.995)]))

def control(ids):
    return dbc.Row([
        dbc.Card(
        [
            dbc.FormGroup(
                [
                    dbc.Label("Temperature"),
                    dcc.RangeSlider(
                        id = f'temp{ids}',
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
                        id = f'hum{ids}',
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
                            id = f'vis{ids}',
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
                            id = f'wind{ids}',
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

kpis = dbc.Row([dbc.Col(dbc.Alert(
        html.H4(
            id='mean_sev'
        ), 
        color = 'danger'  
),md=6,className="text-center"),
dbc.Col(dbc.Alert(
        html.H4(
            id='num_acc'
        ),
        color = "primary"
),md=6,className="text-center"),]
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


page = dbc.Container(
    [
        
        html.H1("US accidents"),
        dbc.Tabs(
        [
            dbc.Tab(label="Main", tab_id="main"),
            dbc.Tab(label="Predictive", tab_id="predictive"),
        ],
        id="tabs",
        active_tab="main",
        ),
        html.Div(id="tab-content", className="p-4"),
        ],
    fluid=True,
)
main = dbc.Container([control(0),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='sev'), md=6),
                dbc.Col(dcc.Graph(id='states'), md=6)
            ]
        ),
        kpis,
        USmap,
])

tour = dbc.Container(
    [
    dbc.Row(
        [
            dbc.Col(
                [
                    control(1),
                    dbc.CardBody(
                        [
                            html.P(
                                id='predict1'
                            )
                        ]
                    ),
                    html.Hr(),
                    control(2),
                    dbc.CardBody(
                        [
                            html.P(
                                id='predict2'
                            )
                        ]
                    ),
                ],
                md=5
            ),
            dbc.Col([],md=2),
            dbc.Col(
                [
                    control(3),
                    dbc.CardBody(
                        [
                            html.P(
                                id='predict3'
                            )
                        ]
                    ),
                    html.Hr(),
                    control(4),
                    dbc.CardBody(
                        [
                            html.P(
                                id='predict4'
                            )
                        ]
                    ),
                ],
                md=5
            )
        ]
    )
    ]
)