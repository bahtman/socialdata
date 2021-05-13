import pandas as pd
import numpy as np
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile



def getDF():
    data = pd.read_csv("./CleanedData.zip")

    return data

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