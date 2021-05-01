#importing required libraries
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import py_functions

# some useful functions
def satisfaction(x):
    if x=='satisfied' :
        return 1 
    else :
        return 0

#loading data
df2=p.read_csv(r"C:/Users/sai/Desktop/shiva/shiva_studies/ML/projects/passenger_satisfaction/ml_model/satisfaction_2015.csv")

#separating class labels and train variable
target = df2['satisfaction_v2'].copy()
df2 = df2.drop(['satisfaction_v2'],axis=1)
print(df2.shape)
print(target.shape)

# label encoding class labels
target = target.map(satisfaction)

# preprocessing data
df2 = py_functions.rename_func(df2)
df2 = py_functions.preprocessing(df2)

# train-test split and model training
xtr, xtest, ytr, ytest = train_test_split(df2, target ,train_size=0.8, test_size=0.2)
clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=10, random_state=42, n_jobs=-1)
clf.fit(xtr,ytr)
print(xtr.shape)
print(xtr.columns)

# pickling model
filename = 'finalized_model_satisfaction.sav'
joblib.dump(clf, filename)
