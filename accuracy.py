from DataPreperation import DataPreprocessing
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataprep = DataPreprocessing()
models = {
            'AdaBoost': AdaBoostClassifier(algorithm='SAMME'),
            'Random Forest': RandomForestClassifier(),
            'Decision Tree': DecisionTreeClassifier(),
            'Logistic Regression': LogisticRegression(),
            'Naive Bayes': GaussianNB(),
            'Support Vector Machine': SVC(),
            'XGBoost': xgb.XGBClassifier()
        }

x_train, x_test, y_train, y_test = dataprep.preprocess_data()
accuracies=[]
for name, model in models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

#mean_value = sum(accuracies)/len(accuracies)
#print("Mean Accuracy of all Models: ", mean_value)
#0.8857142857142856
#0.8857142857142856
#0.8878048780487804
#value = ((0.8857142857142856 + 0.8857142857142856 + 0.8878048780487804)/3)*100
#print(value)

### the Accuracy is 88.64 %
confussions = {}
for i in range(0, 4):
    for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        precission = confusion_matrix(y_test, y_pred)
        confussions[name] = precission

value = np.mean(list(confussions.values()), axis=0)
plt.figure(figsize=(6, 4))
sns.heatmap(value, annot=True, fmt='.1f', cmap='Blues')
plt.title('confusion matrix')
plt.xlabel('predicted labels')
plt.ylabel('True lables')
plt.show()



#mean_value = sum(precissions)/len(precissions)
#print(mean_value)

#0.8891215648466014
#0.8911524259715392
#0.8891215648466014

#value = ((0.8891215648466014 + 0.8911524259715392 + 0.8891215648466014) / 3) * 100
#print('Weighted Average Precision: ', value)

### the Precission of this application is 88.98%