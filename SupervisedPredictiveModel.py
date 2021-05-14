import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
data = pd.read_csv("data/DataForModel.csv")
Weather_Conditions = data['Weather_Condition'].unique()
data['Weather_Condition'] = data['Weather_Condition'].astype('category')
data['Weather_Condition_Encoded'] = data['Weather_Condition'].cat.codes
data_subset = data.drop(['Month', 'Source','TMC','Start_Lat','Start_Lng','State','Unnamed: 0'] ,axis = 1, inplace = False)

train_df, test_df = train_test_split(data_subset, test_size=0.2)

#Define train X and y train set
X_train = train_df.drop(labels = ['Severity'], axis = 1, inplace = False)
y_train = train_df['Severity']

#Define train X and y test set
X_test = test_df.drop(labels = ['Severity'], axis = 1, inplace = False)
y_test = test_df['Severity']

#Scale train set
X_train = X_train[['Visibility','Wind_Speed','Humidity','Temperature']]
#scaler = preprocessing.StandardScaler().fit(X_train_scaled)
#_train_scaled = scaler.transform(X_train_scaled)

#Scale test set_
X_test = X_test[['Visibility','Wind_Speed','Humidity','Temperature']]
#scaler = preprocessing.StandardScaler().fit(X_test_scaled)
#X_test_scaled = scaler.transform(X_test_scaled)

#Define and train model

model = LogisticRegression(solver='lbfgs', max_iter=10000)
model.fit(X_train, y_train)
yhat = model.predict(X_test)
acc = accuracy_score(y_test, yhat)
print(acc)

filename = 'SupervisedPredictiveModel.pickle'
pickle.dump(model, open(filename, 'wb'))

X_test_df = pd.DataFrame(X_test, columns = ['Visibility','Wind_Speed','Humidity','Temperature'])
y_test_df = pd.DataFrame(y_test, columns = ['Severity'])

X_test_df.to_csv('X_test.csv')
y_test_df.to_csv('y_test.csv')

ynew = model.predict(X_test)
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)