import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
data = pd.read_csv("DataForModel.csv")
data_subset = data[['Visibility','Wind_Speed','Humidity','Temperature']]

train_df, test_df = train_test_split(data_subset, test_size=0.2)

#Define train X and y train set
X_train = train_df.drop(labels = ['Severity'], axis = 1, inplace = False)
y_train = train_df['Severity']

#Define train X and y test set
X_test = test_df.drop(labels = ['Severity'], axis = 1, inplace = False)
y_test = test_df['Severity']


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