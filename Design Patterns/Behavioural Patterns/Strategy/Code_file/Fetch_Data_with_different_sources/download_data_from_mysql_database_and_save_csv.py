# Importing Libraries used in this module
from abc import ABCMeta

# Importing third party library
from .download_data_and_write_in_csv import DownloadDataAndSaveInCsv
from Save_file_in_csv_formate.save_file_in_csv_format import SaveDataInCSVFormat


class DownloadDataFromMysqlDatabaseAndSaveInCsv(DownloadDataAndSaveInCsv, metaclass=ABCMeta):
    def __init__(self, database_conn_object, table_name):
        super().__init__(database_conn_object)
        self._conn_object = database_conn_object
        self._table_name = table_name

    def download_data_and_save(self):
        _query = f"""
                    SELECT * 
                    FROM {self._table_name} 
                """
        print(_query)
        my_cursor = self._conn_object.cursor()
        my_cursor.execute(_query)
        result = my_cursor.fetchall()

        record = [data for data in result]
        SaveDataInCSVFormat(record, "data_database").save_data_in_csv()