import pandas as pd

data = pd.read_csv("us-accidents.zip")
data.info()
data['Temperature'] = data['Temperature(F)'].apply(lambda x: (x-32)*5/9)
data['Wind_Chill'] = data['Wind_Chill(F)'].apply(lambda x: (x-32)*5/9)
data['Visibility'] = data['Visibility(mi)'].apply(lambda x: x*1.609344)
data['Wind_Speed'] = data['Wind_Speed(mph)'].apply(lambda x: x*1.609344*1000/3600)
data['Humidity'] = data['Humidity(%)']
CleanedData = data.drop(['Number',"Weather_Condition","End_Time","Temperature(F)","Wind_Chill(F)","Visibility(mi)","Wind_Speed(mph)","Humidity(%)","Description","City","County","Zipcode","Timezone","Weather_Timestamp",'Distance(mi)','Airport_Code','Street','Side','Country','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Civil_Twilight','Nautical_Twilight','Astronomical_Twilight', 'End_Lat','End_Lng'],axis='columns', inplace=False)
CleanedDataV2 = CleanedData.dropna()

CleanedDataV2.info()

#Hvis en ny fil skal gemmes:
CleanedDataV2.to_csv('CleanedData.csv')