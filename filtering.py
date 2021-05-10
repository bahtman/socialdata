import pandas as pd
import numpy as np

import folium
from folium.features import DivIcon

from sklearn import preprocessing


def getDF(filename):

    # Read the data into a dataframe
    full_df = pd.read_csv(filename)

    return full_df

full_df = getDF("data/accidents.csv")

def get_nbdgroups():
    """
    This function returns a dictionary of Neighborhood groups to populate a selection filter
    Input: None
    Returns: Dictionary
    """
    nbd_groups = list(full_df.neighbourhood_group_cleansed.unique())
    nbd_groups.sort()
    return ["All"] + nbd_groups