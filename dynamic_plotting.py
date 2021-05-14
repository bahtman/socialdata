import pandas as pd
import numpy as np

import folium
import folium.plugins
from folium.plugins import HeatMap
import plotly.express as px

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
        location=[40, -100],#location=[df["Start_Lat"].mean(), df['Start_Lng'].mean()],
        tiles="CartoDB positron",
        zoom_start=4,
    )
    values = df[['Start_Lat','Start_Lng']].values

    HeatMap(values, radius=5,blur=2).add_to(folium.FeatureGroup(name='Heat Map').add_to(this_map))
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

def plotstates(filtered_df):
    #Plot hyppighed pr. inbygger:
    GroupedDataHyp = filtered_df.groupby(['State']).count()
    temp = []
    population = {'AL': 4903185, 'AR': 3017825, 'AZ': 7278717, 'CA': 39512223, 'CO': 5758736, 'CT':3565287, 'DC': 705749, 'DE': 973764, 'FL': 21477737, 'GA': 10617423, 'IA': 3155070, 'ID': 1787065, 'IL': 12671821, 'IN': 6732219, 'KS': 2913314, 'KY': 4467673, 'LA': 4648794, 'MA': 6949503, 'MD': 6045680, 'ME': 1344212, 'MI': 9986857, 'MN': 5639632, 'MO': 6137428, 'MS': 2976149, 'MT': 1059778, 'NC': 10488084, 'ND': 762062, 'NE': 1934408, 'NH': 1359711, 'NJ': 8882190, 'NM': 2096829, 'NV': 3080156, 'NY': 19453561, 'OH': 11789100, 'OK': 3956971, 'OR': 4217737, 'PA': 12801989, 'RI': 1059361, 'SC': 5148714, 'SD': 884659, 'TN': 6833174, 'TX': 28995881, 'UT': 3205958, 'VA': 8535519, 'VT': 623989, 'WA': 7614893, 'WI': 5822434, 'WV': 1792147, 'WY': 578759}
    GroupedDataHyp = GroupedDataHyp.iloc[:,0].reset_index(name='Count')
    for i in range(len(GroupedDataHyp)):
        temp.append(population[GroupedDataHyp['State'].iloc[i]])
    GroupedDataHyp['population'] = temp
    GroupedDataHyp['normalized'] = GroupedDataHyp['Count'].div(GroupedDataHyp['population']*0.0001)
    return px.bar(GroupedDataHyp, x='State', y ='normalized')

def plotsev(filtered_df):
    #Plot hyppighed af severity:
    GroupedDataServerity = filtered_df.groupby(['Severity']).count()
    GroupedDataServerity = GroupedDataServerity.iloc[:,0].reset_index(name='Count')
    return px.bar(GroupedDataServerity, x='Severity', y ='Count')