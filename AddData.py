from DataPreperation import DataPreprocessing
from ModelTraining import ModelTraining
import csv

class AddData():
    def __init__(self):
        self.dataprep = DataPreprocessing()
        self.mt = ModelTraining()

    def add_new_data(self, new_data):
        csv_path = 'code/dataset/heart1.csv'
        with open(csv_path, mode='a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)
            self.dataprep.preprocess_data()
            self.mt.train_models()