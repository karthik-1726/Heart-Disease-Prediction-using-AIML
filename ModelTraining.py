from DataPreperation import DataPreprocessing
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.metrics import accuracy_score as As

class ModelTraining:
    def __init__(self):
        self.dataprep = DataPreprocessing()
        self.models = {
            'AdaBoost': AdaBoostClassifier(algorithm='SAMME'),
            'Random Forest': RandomForestClassifier(),
            'Decision Tree': DecisionTreeClassifier(),
            'Logistic Regression': LogisticRegression(),
            'Naive Bayes': GaussianNB(),
            'Support Vector Machine': SVC(),
            'XGBoost': xgb.XGBClassifier()
        }

    def train_models(self):
        x_train, x_test, y_train, y_test = self.dataprep.preprocess_data()
        trained_models = {}
        for name, model in self.models.items():
            model.fit(x_train, y_train)  # Fit the model first
            y_pred = model.predict(x_test)
            accuracy = As(y_test, y_pred)
            trained_models[name] = accuracy
            filename = f'{name}_model.joblib'
            self.dataprep.SaveModel(model,filename)
        return trained_models

    def Select_best_model(self, accuracy):
        best_accuracy = max(accuracy.values())
        return best_accuracy
        
#for testing and training the model the module 

#mt = ModelTraining()
#url = "dataset/heart.csv"
#trained_models = mt.train_models()
#mt.Select_best_model(trained_models)
#print("Trained models:", trained_models)
