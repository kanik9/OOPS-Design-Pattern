# Importing Libraries used in this module
import json
from abc import ABCMeta

# Importing third party library
from .download_data_and_write_in_csv import DownloadDataAndSaveInCsv
from Save_file_in_csv_formate.save_file_in_csv_format import SaveDataInCSVFormat


class DownloadDataFromApiAndSaveInCsv(DownloadDataAndSaveInCsv, metaclass=ABCMeta):
    def __init__(self, api_conn_object):
        super().__init__(api_conn_object)
        self._conn_object = api_conn_object

    def download_data_and_save(self):
        record = self._conn_object.json()
        record = record["data"]
        SaveDataInCSVFormat(record, "data_api").save_data_in_csv()