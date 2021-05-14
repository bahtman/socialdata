from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
import pickle
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("data/DataForModel.csv")
new_severity2_n = int(0.3*len(data['Severity']))
data_subset = data.drop(['Month', 'Source','TMC','Start_Lat','Start_Lng','State','Unnamed: 0','Weather_Condition'] ,axis = 1, inplace = False)
Severity2_down = data_subset[data_subset['Severity']==2][0:new_severity2_n]

Data_set_finished = pd.concat([data_subset[data_subset['Severity']==1],Severity2_down,data_subset[data_subset['Severity']==3],data_subset[data_subset['Severity']==4]])
X = Data_set_finished.drop(labels = ['Severity'], axis = 1, inplace = False)
y = Data_set_finished['Severity']
X_train, X_test, y_train , y_test= train_test_split(X,y, test_size=1/3, random_state=100)

regr = RandomForestRegressor(max_depth=3, random_state=42)
regr.fit(X_train, y_train)

yhat = regr.predict(X_test)

MSE = mean_squared_error(y_test, yhat)
print(MSE)
filename = 'RandomForrestModel.sav'
pickle.dump(regr, open(filename, 'wb'))

### If we want to hyperparameter tuning
X_train, y_train = make_regression(n_features=4, n_informative=2,
                         random_state=0, shuffle=False)
model = RandomForestRegressor(max_depth=2, random_state=0)

param_grid = {
    'min_samples_split': [100,300,900],#[100,200,300,400,500,600,700,800,900,1000],
    'n_estimators': [200,4000,10000]#[100,250,500,1000,2000,3000,4000,5000,10000]
}


clf = GridSearchCV(model, param_grid= param_grid,return_train_score=True, scoring='accuracy',verbose=1,n_jobs=-1)
clf.fit(X_train,y_train)

#Process the data from CV
test_scores = clf.cv_results_['mean_test_score']
train_scores = clf.cv_results_['mean_train_score'] 
n_trees = list(clf.cv_results_['param_n_estimators'])
min_samples = list(clf.cv_results_['param_min_samples_split'])
CV_data = pd.DataFrame(data={'test':test_scores,'train':train_scores,'trees':n_trees,'min_samples':min_samples})
tree_data = CV_data.groupby('trees').mean()
sample_data = CV_data.groupby('min_samples').mean()



#Plot the accuracy curves for the two parameters
plt.subplots(1, 2, figsize=(10, 6))
plt.subplot(121)
plt.plot(tree_data.index, tree_data['train'], '.-', label = 'train')
plt.plot(tree_data.index, tree_data['test'], '.-', label = 'test')

plt.legend()
plt.xlabel("Number of estimators [1]")
plt.ylabel('Accuracy [%]')
plt.title('Accuracy vs. Number of trees')

plt.subplot(122)
plt.plot(sample_data.index, sample_data['train'], '.-', label = 'train')
plt.plot(sample_data.index, sample_data['test'], '.-', label = 'test')
plt.legend()
plt.xlabel("Minimum sample in split [1]")
plt.ylabel('Accuracy [%]')
plt.title('Accuracy vs. Min split size')
    
    
plt.tight_layout(pad = 4)

###
