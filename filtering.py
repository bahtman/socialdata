import pandas as pd
import numpy as np

import folium
from folium.features import DivIcon

from sklearn import preprocessing
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile



def getDF():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('sobhanmoosavi/us-accidents')


    zf = ZipFile('us-accidents.zip')
    zf.extractall('data/') #save files in selected folder
    zf.close()

    data = pd.read_csv("./data/US_Accidents_Dec20_Updated.csv")
    CleanedData = data.drop(['End_time','Description','County','Zipcode','Weather_Timestamp','Wind_Direction','Number','Distance(mi)','Airport_Code','Street','Side','Country','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight', 'End_Lat','End_Lng'],axis='columns', inplace=False)
    CleanedDataV2 = CleanedData.dropna()

    return CleanedDataV2

full_df = getDF()

def get_weathergroups():
    """
    This function returns a List of Weather condition groups to populate a selection filter
    Input: None
    Returns: List
    """
    weather_groups = list(full_df.Weather_Condition.unique())
    weather_groups.sort()
    return ["All"] + weather_groups

def get_stategroups():
    """
    This function returns a List of States to populate a selection filter
    Input: None
    Returns: List
    """
    state_groups = list(full_df.State.unique())
    state_groups.sort()
    return ["All"] + state_groups