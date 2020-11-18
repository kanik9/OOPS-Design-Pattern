# Importing Libraries
from abc import ABC, abstractmethod


class DownloadDataAndSaveInCsv(ABC):
    """
        It is an abstract class which is use to extract data from Source and save the data into a csv file and also return
        data. This class contain 2 methods , __init__() and another method is getData() method both are abstract method.

        1. __init__(self, *args):
            Definition : It is a abstract class constructor which take at most 2 inputs .And it also crate class variable to
                         make handling easy.
                         case 1: only take connection object .
                         case 2: When fetching data from database it take 2 input , first is connection object and second is
                                 table_name to extract data from table by firing query.

            Output : None

        2. download_data_and_save(self):
            Definition : download_data_and_save abstract method is use to fetch data and save this data to csv file .
            For saving data into csv file we use another class whose name is 'SaveDataInCSVFormat' which is define in
            Save_file_in_csv_format folder python package.saveDataInCSVFile. And it also return fetched data  .

            Input: None
            Output : 1. CSV File

        """

    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def download_data_and_save(self):
        pass