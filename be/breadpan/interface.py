from abc import ABCMeta, abstractmethod
from breadpan.usecase import IUsecaseOutputPort


class IController(metaclass=ABCMeta):
    """Interface of data controller class.

    """
    @abstractmethod
    def create(self, **kwargs) -> IUsecaseOutputPort:
        pass

    @abstractmethod
    def read(self,  **kwargs) -> IUsecaseOutputPort:
        pass

    @abstractmethod
    def update(self,  **kwargs) -> IUsecaseOutputPort:
        pass

    @abstractmethod
    def delete(self,  **kwargs) -> IUsecaseOutputPort:
        pass


