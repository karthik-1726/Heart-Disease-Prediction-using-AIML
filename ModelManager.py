import numpy as np
import joblib
#from DataPreperation import DataPreprocessing
from sklearn.metrics import accuracy_score as As
#from ModelTraining import ModelTraining

class ModelManager:
    def __init__(self):
        self.models = {}

    def load_models(self):
        model_path = {
    'AdaBoost': 'Adaboost_model.joblib',
    'RandomForest': 'Random Forest_model.joblib',
    'DecisionTree': 'Decision Tree_model.joblib',
    'LogisticRegression': 'Logistic Regression_model.joblib',
    'Naive Bayes': 'Naive Bayes_model.joblib',
    'SVM': 'Support Vector Machine_model.joblib',
    'XGboost':'XGBoost_model.joblib'
    }
        for model_name, model_path in model_path.items():
            try:
                self.models[model_name] = joblib.load(f'code/models/{model_path}')
            except FileNotFoundError:
                print(f"Model file not found for {model_name}. Please check the file path.")
    
    def predict(self, input_data):
        predictions = {}
        for model_name, model in self.models.items():
            try:
                prediction = model.predict(input_data)
                predictions[model_name] = prediction
            except Exception as e:
                print(f"Error predicting with {model_name}: {str(e)}")
                predictions[model_name] = None
        return predictions

    def get_best_prediction(self, predictions):
        count_0 = 0
        count_1 = 0

        # Iterate through the predictions dictionary
        for prediction in predictions.values():
            if prediction == 0:
                count_0 += 1
            elif prediction == 1:
                count_1 += 1

        # Determine the best prediction based on counts
        best_prediction = 0 if count_0 > count_1 else 1 if count_1 > count_0 else None
        return best_prediction


#for testing the module


#input_data = np.array([0,100,122,0,0,1,0]).reshape(1,-1)
#mm = ModelManager()
#mm.load_models()
#predictions = mm.predict(input_data)
#print(predictions)
#print(mm.get_best_prediction(predictions))


