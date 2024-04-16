import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as ss
import os
import joblib as jl

class DataPreprocessing:
    def __init__(self):
        self.data = None

    def preprocess_data(self):
        self.data = pd.read_csv("code/dataset/heart1.csv")

            # Drop rows with any missing values
        self.data.dropna(axis=0, how='any', inplace=True)

            # Drop columns with any missing values
        self.data.dropna(axis=1, how='any', inplace=True)

            # Split data into features (X) and target (y)
        X = self.data.drop(columns='target')
        y = self.data['target']

            # Split data into train and test sets
        X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=42)

            # Scale features
        scaler = ss()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test


    def SaveModel(self, model, filename):
        # Create directory if it does not exist
        os.makedirs("code/models", exist_ok=True)

        # Remove the existing model file if it exists
        model_file = os.path.join("code/models", filename)
        if os.path.exists(model_file):
            os.remove(model_file)

        # Save the model to the specified filepath
        jl.dump(model, os.path.join("code/models", filename))






    
#for testing the modules

#dataprep = DataPreprocessing()
#dataprep.preprocess_data()