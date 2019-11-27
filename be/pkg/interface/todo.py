
from pkg.interface import IController
from pkg.usecase.todo import ToDoCreateInteractor
from pkg.usecase.todo import ToDoReadInteractor
from pkg.usecase.todo import ToDoDeleteInteractor


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

    def update(self,  **kwargs):
        pass
