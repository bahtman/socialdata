import pandas as pd
import numpy as np
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile



def getDF():
    if not os.path.isfile("./data/US_Accidents_Dec20_Updated.csv"):
        print('her')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files('sobhanmoosavi/us-accidents')
        print("Zip filen: ",os.path.isfile("./us-accidents.zip"))
        print("Zip filen2: ",os.path.isfile("us-accidents.zip"))

        zf = ZipFile('./us-accidents.zip')
        zf.extractall('data/') #save files in selected folder
        zf.close()

    data = pd.read_csv("./data/US_Accidents_Dec20_Updated.csv")
    CleanedData = data.drop(['End_Time','Description','County','Zipcode','Weather_Timestamp','Wind_Direction','Number','Distance(mi)','Airport_Code','Street','Side','Country','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight', 'End_Lat','End_Lng'],axis='columns', inplace=False)
    CleanedData['Temperature'] = CleanedData['Temperature(F)'].apply(lambda x: (x-32)*5/9)
    CleanedData['Wind_Chill'] = CleanedData['Wind_Chill(F)'].apply(lambda x: (x-32)*5/9)
    CleanedData['Visibility'] = CleanedData['Visibility(mi)'].apply(lambda x: x*1.609344)
    CleanedData['Wind_Speed'] = CleanedData['Wind_Speed(mph)'].apply(lambda x: x*1.609344*1000/3600)
    CleanedData['Humidity'] = CleanedData['Humidity(%)']
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