from abc import *

class IUsecaseInputPort(object):
    """Interface of use case input port.

    """
    data = {}

    def __init__(self):
        self.data = {}

    def input(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value



class IUsecaseInteractor(IUsecaseInputPort):
    """IUsecaseInteractor

    """
    @abstractmethod
    def operate(self):
        """operate
        Will return the class inherited from IUsecaseOutputPort.
        """
        pass


class IUsecaseOutputPort(metaclass=ABCMeta):
    """Interface of use case input port.

    """
    data = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value
    
