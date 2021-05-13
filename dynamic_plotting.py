import pandas as pd
import numpy as np

import folium
import folium.plugins
from folium.plugins import HeatMap
import plotly.graph_objs as go

from filtering import *

def filterdf(temp, humid, vis, wind):
    filtered_df = full_df[full_df['Temperature'].between(temp[0],temp[1])].copy()
    filtered_df = filtered_df[filtered_df['Humidity'].between(humid[0],humid[1])]
    filtered_df = filtered_df[filtered_df['Visibility'].between(vis[0],vis[1])]
    filtered_df = filtered_df[filtered_df['Wind_Speed'].between(wind[0],wind[1])]


    return filtered_df
def createMap(df):
    """
    This function takes in a dataframe and applies a fucntion that creates circle markers for every 
        latitude and longitude in the dataframe

    Args:
        df ([dataframe]): [Dataframe containing latitude and longitude as well as column nbd_count_normalized
                            for count of listings normalized ]
        fixed_radius ([boolean]): [if true use 30 as fixed radius, if false use the count to determine size of circle]
        nbd_or_grp ([String]): [neighbourhood/group]

    Returns:
        [Folium Map]: [Folium map]
    """
    # Initialize a Folium map. Center it to the mean of latitude and longitude of the entire dataset
    this_map = folium.Map(
        location=[df["Start_Lat"].mean(), df['Start_Lng'].mean()],
        tiles="CartoDB positron",
        zoom_start=5,
    )
    values = df[['Start_Lat','Start_Lng']].values

    HeatMap(values, radius=10,blur=5).add_to(folium.FeatureGroup(name='Heat Map').add_to(this_map))
    folium.LayerControl().add_to(this_map)
    return this_map

def saveAccidentMapHTML(filtered_df):
    """
        Call this function to create the HTML of the individual listings  map
        Input : Neighborhood group 
        Returns : a filename of the folium map created and saved 
    """
    # TBD Add an all and then use All or nbd to filter the dataframe (create a copy of it)

    this_map = createMap(filtered_df)

    filename = (
        "Maps/Accidentmap.html"
    )
    this_map.save(filename)
    return filename

def getAvgSeverity(filtered_df):
    """
        Call this function to get average price(rent) in the neighborhood group
        Input : Neighborhood group 
        Returns : Average price  of listings in neighborhood group
    """
    return np.round(filtered_df["Severity"].mean(), 2)