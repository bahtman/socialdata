import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from filtering import *
from layout2 import *
from dynamic_plotting import *


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#saveAccidentMapHTML("All")
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])




@app.callback(
       dash.dependencies.Output('accident_map', 'srcDoc'),
       [
       dash.dependencies.Input('temp', 'value'),
       dash.dependencies.Input('hum', 'value'),
       dash.dependencies.Input('vis', 'value'),
       dash.dependencies.Input('wind', 'value'),
       ]
       
)
def update_chart(temp, humid, vis, wind):
    filtered_df = filterdf(temp, humid, vis, wind)
    filename = saveAccidentMapHTML(filtered_df)
    #filename='Maps/Accidentmap.html'
    return  open(filename, 'r').read()

@app.callback(
       dash.dependencies.Output('mean_sev', 'children'),
       [
       dash.dependencies.Input('temp', 'value'),
       dash.dependencies.Input('hum', 'value'),
       dash.dependencies.Input('vis', 'value'),
       dash.dependencies.Input('wind', 'value')
       ]
       
)
def update_chart(temp, humid, vis, wind ):   
    filtered_df = filterdf(temp, humid, vis, wind)
    return f"{getAvgSeverity(filtered_df)} \n Average severity"   

@app.callback(
       dash.dependencies.Output('num_acc', 'children'),
       [
       dash.dependencies.Input('temp', 'value'),
       dash.dependencies.Input('hum', 'value'),
       dash.dependencies.Input('vis', 'value'),
       dash.dependencies.Input('wind', 'value')
       ]
       
)
def update_chart(temp, humid, vis, wind ):   
    filtered_df = filterdf(temp, humid, vis, wind)
    return f"{filtered_df.shape[0]} \n accidents"    

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return main # This is the "home page"

if __name__ == '__main__':
    app.run_server(debug=True)