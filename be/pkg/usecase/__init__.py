from abc import *


class IUsecaseInputPort:
    """Interface of use case input port.

    """
    data = {}

    def __init__(self):
        self.data = {}

    def input(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value


class IUsecaseOutputPort(metaclass=ABCMeta):
    """Interface of use case input port.

    """
    data = {}
    @classmethod
    def output(cls, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value


class IUseCaseInteractor(IUsecaseInputPort):
    """IUseCaseInteractor

    """

    def operate(self) -> IUsecaseOutputPort:
        return None
