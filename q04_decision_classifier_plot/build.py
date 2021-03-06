# default imports
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("./data/loan_prediction.csv")
np.random.seed(9)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

depth_list = [8, 10, 15, 20, 50, 100, 120, 150, 175, 200]

def decision_classifier_plot(X_train,X_test,y_train,y_test,depth_list):
    a=[]
    b=[]
    for i in depth_list:
        dtc = DecisionTreeClassifier(random_state=9,max_depth=i)
        dtc.fit(X_train,y_train)
        y_train_pred = dtc.predict(X_train)
        y_test_pred = dtc.predict(X_test)
        acc1 = accuracy_score(y_train,y_train_pred)
        a.append(acc1)
        acc2 = accuracy_score(y_test,y_test_pred)
        b.append(acc2)

    plt.plot(depth_list,a)
    plt.plot(depth_list,b)
    plt.show()
