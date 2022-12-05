import pandas as pd


def extract_from_csv(path):
    dataframe = pd.read_csv(path)
    return dataframe
