# Importing Libraries to be used in this module
import requests
from abc import ABCMeta

# Importing third party module
from .connect_to_source import ConnectToSource


class ConnectToRemoteUrl(ConnectToSource, metaclass=ABCMeta):
    def __init__(self, conn_url):
        super().__init__(conn_url)
        self._source_conn_url = conn_url

    def connect_to_source(self):
        try:
            with requests.Session() as s:
                connection = s.get(self._source_conn_url)
            return connection
        except Exception as e:
            error = {
                "Error/Warning": e
            }
            print(error)
