from src.config import settings
from src.plugins.csv_plugin import extract_from_csv


class ExtractAgent:
    def extract_by_plugin(self):
        if settings.PLUGIN == 'csv':
            return extract_from_csv(settings.CSV_FILE_PATH)
        elif settings.PLUGIN == 'prometheus':
            pass
