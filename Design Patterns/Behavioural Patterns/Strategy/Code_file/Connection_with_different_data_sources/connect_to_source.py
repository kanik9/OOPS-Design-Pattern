from abc import ABC, abstractmethod


class ConnectToSource(ABC):
    """
        It is an abstract class which is used in connection establishing with source . It contain two methods in which
        __init__ is a constructor and a connect is a method which is responsible to make connection.

        1. __init__(self, conn):
            Definition : It is abstract method(constructor) of a abstract class(ConnectToSource)  whose work is to create
            class variable . The class variable make variable handling easy .
            Input : 'conn' it is a connection string of data source from which connection is created.
            Output : None

        2. connect_to_source(self):
            Definition : It is the another abstract method of abstract class(ConnectToSource) which use class variable of
                         connection string to make connection and help in fetching the data from source.
            Input : None
            Output : Connection object

        """
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def connect_to_source(self):
        pass