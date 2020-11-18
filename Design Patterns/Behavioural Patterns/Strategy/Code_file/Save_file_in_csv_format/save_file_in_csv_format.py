import pandas as pd


class SaveDataInCSVFormat:
    """
    It is a class which is use to save data in CSV file which is stored in Data_storage folder. It uses pandas .
    """
    def __init__(self, data, file_name):
        self._data = data
        self._file_format = "csv"
        self._file_name = file_name
        self._file_store_location = None
        self._storage_location = f"{self._file_store_location}{self._file_name}.{self._file_format}"

    def save_data_in_csv(self):
        _data_object = pd.DataFrame(self._data)
        _data_object.to_csv(self._storage_location)
