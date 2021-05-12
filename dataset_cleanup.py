import pandas as pd

data = pd.read_csv("data/US_Accidents_Dec20.csv")
CleanedData = data.drop(['Number','Distance(mi)','Airport_Code','Street','Side','Country','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight', 'End_Lat','End_Lng','Precipitation(in)'],axis='columns', inplace=False)
data.info()

CleanedDataV2 = CleanedData.dropna()

CleanedDataV2.info()

#Hvis en ny fil skal gemmes:
compression_opts = dict(method='zip',archive_name='CleanedData.csv')  
CleanedDataV2.to_csv('CleanedData.zip', compression=compression_opts)