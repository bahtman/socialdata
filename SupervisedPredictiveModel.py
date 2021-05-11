import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
data = pd.read_csv("data/CleanedData.csv")

X = data.drop(labels = ['Severity'], axis = 1, inplace = False)
y = data['Severity']

X_scaled = X[['Visibility(mi)','Wind_Speed(mph)','Pressure(in)','Humidity(%)','Temperature(F)']]
scaler = preprocessing.StandardScaler().fit(X_scaled)
X_scaled = scaler.transform(X_scaled)

#Forsøg 1
clf = LogisticRegression(random_state=0).fit(X_scaled, y)
clf.predict(X[:2, :])
clf.predict_proba(X[:2, :])
clf.score(X, y)

#Forsøg 2

model = LogisticRegression(solver='lbfgs')
model.fit(X_scaled, y)
yhat = model.predict(X_scaled)
acc = accuracy_score(y, yhat)
print(acc)