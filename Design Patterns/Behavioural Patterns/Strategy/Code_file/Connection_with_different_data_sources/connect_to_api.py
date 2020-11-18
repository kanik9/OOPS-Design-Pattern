# Importing Libraries to be used in this module
import requests
from abc import ABCMeta

# Importing third party module
from .connect_to_source import ConnectToSource


class ConnectToApi(ConnectToSource, metaclass=ABCMeta):
    def __init__(self, api_url):
        super().__init__(api_url)
        self._source_api_url = api_url

    def connect_to_source(self):
        try:
            conn = requests.request("GET", self._source_api_url)
            return conn
        except Exception as e:
            error = {
                "Error/Warning": e
            }
            print(error)
