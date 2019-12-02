from abc import ABCMeta, abstractmethod
from breadpan.usecase import IUsecaseOutputPort

class IPresenter(IUsecaseOutputPort):
    def __init__(self, output_port: IUsecaseOutputPort):
        self.data = output_port.data
        # To-Do: Do any operation additionally.


class IController(metaclass=ABCMeta):
    """Interface of data controller class.

    """
    @abstractmethod
    def create(self, **kwargs) -> IPresenter:
        pass

    @abstractmethod
    def read(self,  **kwargs) -> IPresenter:
        pass

    @abstractmethod
    def update(self,  **kwargs) -> IPresenter:
        pass

    @abstractmethod
    def delete(self,  **kwargs) -> IPresenter:
        pass


