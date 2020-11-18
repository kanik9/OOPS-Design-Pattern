# Importing Libraries used in this module
import csv
from abc import ABCMeta

# Importing third party library
from .download_data_and_write_in_csv import DownloadDataAndSaveInCsv
from Save_file_in_csv_formate.save_file_in_csv_format import SaveDataInCSVFormat


class DownloadDataFromRemoteUrlAndSaveInCsv(DownloadDataAndSaveInCsv, metaclass=ABCMeta):
    def __init__(self, remote_url_conn_object):
        super().__init__(remote_url_conn_object)
        self._conn_object = remote_url_conn_object

    def download_data_and_save(self):
        decoded_content = self._conn_object.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data_dict = list(cr)
        SaveDataInCSVFormat(data_dict, "data_csv").save_data_in_csv()
