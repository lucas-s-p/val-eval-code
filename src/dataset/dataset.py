import argparse
import pandas as pd

class DatasetLoader:
    def __init__(self, params={}):
        self.params = params

    def load(self):
        file_path = self.params['dataset']
        if file_path.endswith(".parquet"):
            data = pd.read_parquet(self.params['dataset'])
            df = pd.read_csv('./dataset/prediction.csv')
            data['prediction'] = df['prediction']
            data = data.astype(str)
            return data
        elif file_path.endswith(".csv"):
            data = pd.read_csv(self.params['dataset'])
            df = pd.read_csv('./dataset/prediction.csv')
            data['prediction'] = df['prediction']
            data = data.astype(str)
            return data
        else:
            raise ValueError("Unsupported file format. Use a Parquet or CSV file instead.")
        