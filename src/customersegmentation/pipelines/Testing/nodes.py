"""
This is a boilerplate pipeline 'Testing'
generated using Kedro 0.19.1
"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import pickle
def test(df):
    X = df.drop(['Cluster'],axis=1)
    y= df[['Cluster']]
    X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2)     
    model= DecisionTreeClassifier(criterion="entropy")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(metrics.confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
   
   