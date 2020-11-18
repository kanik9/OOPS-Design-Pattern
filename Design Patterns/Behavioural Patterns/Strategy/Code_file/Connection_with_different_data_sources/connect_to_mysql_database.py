# Importing Libraries to be used in this module
import mysql.connector
from abc import ABCMeta
from mysql.connector.errors import Error

# Importing third party module
from .connect_to_source import ConnectToSource


class ConnectToMySqlDatabase(ConnectToSource, metaclass=ABCMeta)
    def __init__(self, database_conn_dict):
        super().__init__(database_conn_dict)
        self._conn_string = database_conn_dict

    def connect_to_source(self):
        try:
            conn_object = mysql.connector.connect(user=self._conn_string["user"],
                                                  password=self._conn_string["password"],
                                                  host=self._conn_string["host"],
                                                  database=self._conn_string["database"],
                                                  port=self._conn_string["port"])
            return conn_object
        except Error as err:
            error = {
                "Error/Warning": err
            }
            print(error)

