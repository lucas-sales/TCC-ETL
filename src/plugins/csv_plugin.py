import pandas as pd

from src.services.transform.trasform_csv import parse_dataframe


def extract_from_csv(path) -> list[dict]:
    dataframe = pd.read_csv(path)
    parsed_data = parse_dataframe(dataframe)
    return parsed_data
