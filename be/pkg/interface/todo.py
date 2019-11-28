
from be.pkg.interface import IController
from be.pkg.usecase import IUsecaseOutputPort, IUsecaseInteractor
from be.pkg.usecase.todo import ToDoCreateInteractor
from be.pkg.usecase.todo import ToDoReadInteractor
from be.pkg.usecase.todo import ToDoDeleteInteractor


class ToDoPresenter(IUsecaseOutputPort):
    def __init__(self, **kwargs):
        super(IUsecaseOutputPort,self).__init__(**kwargs)
    # To-Do: Do any operation additionally.


class ToDoController(IController):
    def create(self, task_id, contents):
        i = ToDoCreateInteractor()
        i.input(task_id=task_id, contents=contents)
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
