import argparse
import pandas as pd

class DatasetLoader:
    """Classe para carregar o dataset."""
    def __init__(self, params={}):
        self.params = params

    def load(self):
        """Carrega o dataset com base no tipo de arquivo."""
        file_path = self.params['dataset']
        if file_path.endswith(".parquet"):
            return pd.read_parquet(self.params['dataset'])
        elif file_path.endswith(".csv"):
            return pd.read_csv(self.params['dataset'])
        else:
            raise ValueError("Formato de arquivo não suportado. Use um arquivo Parquet ou CSV.")
