import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from filtering import *
from layout2 import *
from dynamic_plotting import *


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])



def controlinput(ids):
    return    [
       dash.dependencies.Input(f'temp{ids}', 'value'),
       dash.dependencies.Input(f'hum{ids}', 'value'),
       dash.dependencies.Input(f'vis{ids}', 'value'),
       dash.dependencies.Input(f'wind{ids}', 'value')
       ]

@app.callback(
       dash.dependencies.Output('mean_sev', 'children'),
       controlinput(0)
       
)
def update_chart(temp, humid, vis, wind ):   
    filtered_df = filterdf(temp, humid, vis, wind)
    return f"{getAvgSeverity(filtered_df)} \n Average severity"   

@app.callback(
       dash.dependencies.Output('num_acc', 'children'),
       controlinput(0)
       
)
def update_chart(temp, humid, vis, wind ):   
    filtered_df = filterdf(temp, humid, vis, wind)
    return f"{filtered_df.shape[0]:,} \n accidents"    

@app.callback(
       dash.dependencies.Output('states', 'figure'),
       controlinput(0)
       
)
def update_chart(temp, humid, vis, wind ):   
    filtered_df = filterdf(temp, humid, vis, wind)
    return plotstates(filtered_df)

@app.callback(
       dash.dependencies.Output('sev', 'figure'),
       controlinput(0)
       
)
def update_chart(temp, humid, vis, wind ):   
    filtered_df = filterdf(temp, humid, vis, wind)
    return plotsev(filtered_df)


@app.callback(
       dash.dependencies.Output('Accident_map', 'srcDoc'),
       controlinput(0)
       
)
def update_chart(temp, humid, vis, wind):
    filtered_df = filterdf(temp, humid, vis, wind)
    filename = saveAccidentMapHTML(filtered_df)
    #filename='Maps/Accidentmap.html'
    return  open(filename, 'r').read()
@app.callback(
    dash.dependencies.Output("tab-content", "children"),
    [dash.dependencies.Input("tabs", "active_tab")],
)
def render_tab_content(active_tab):
    if active_tab == "main":
        return main
    else:
        return tour


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return page # This is the "home page"

if __name__ == '__main__':
    app.run_server(debug=True)