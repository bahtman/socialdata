import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
data = pd.read_csv("data/CleanedData.csv")
Weather_Conditions = data['Weather_Condition'].unique()
data['Weather_Condition'] = data['Weather_Condition'].astype('category')
data['Weather_Condition_Encoded'] = data['Weather_Condition'].cat.codes

train_df, test_df = train_test_split(data, test_size=0.2)

#Define train X and y train set
X_train = train_df.drop(labels = ['Severity'], axis = 1, inplace = False)
y_train = train_df['Severity']

#Define train X and y test set
X_test = test_df.drop(labels = ['Severity'], axis = 1, inplace = False)
y_test = test_df['Severity']

#Scale train set
X_train_scaled = X_train[['Visibility(mi)','Wind_Speed(mph)','Pressure(in)','Humidity(%)','Temperature(F)','Weather_Condition_Encoded']]
scaler = preprocessing.StandardScaler().fit(X_train_scaled)
X_train_scaled = scaler.transform(X_train_scaled)

#Scale test set_
X_test_scaled = X_test[['Visibility(mi)','Wind_Speed(mph)','Pressure(in)','Humidity(%)','Temperature(F)','Weather_Condition_Encoded']]
scaler = preprocessing.StandardScaler().fit(X_test_scaled)
X_test_scaled = scaler.transform(X_test_scaled)

#Forsøg 2

model = LogisticRegression(solver='lbfgs')
model.fit(X_train_scaled, y_train)
yhat = model.predict(X_test_scaled)
acc = accuracy_score(y_test, yhat)
print(acc)