
from be.pkg.usecase import ToDoCreateInteractor
from be.pkg.usecase import ToDoReadInteractor
from be.pkg.usecase import ToDoDeleteInteractor


class ToDoController(IController):
    def create(self,  **kwargs):
        i = ToDoCreateInteractor()
        i.input(kwargs)
        return i.operate()

    def read(self,  **kwargs):
        i = ToDoReadInteractor()
        i.input(kwargs)
        return i.operate()

    def delete(self,  **kwargs):
        i = ToDoDeleteInteractor()
        i.input(kwargs)
        return i.operate()
