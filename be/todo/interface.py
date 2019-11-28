from breadpan.interface import IController
from breadpan.usecase import IUsecaseOutputPort, IUsecaseInteractor
from todo.usecase import ToDoCreateInteractor, ToDoReadInteractor, ToDoDeleteInteractor


class ToDoPresenter(IUsecaseOutputPort):
    def __init__(self, **kwargs):
        super(IUsecaseOutputPort,self).__init__(**kwargs)
        # To-Do: Do any operation additionally.


class ToDoController(IController):
    def create(self, todo_id, contents):
        i = ToDoCreateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return i.operate()

    def read(self, todo_id):
        i = ToDoReadInteractor()
        i.input(todo_id=todo_id)
        return i.operate()

    def delete(self, todo_id):
        i = ToDoDeleteInteractor()
        i.input(todo_id=todo_id)
        return i.operate()

    def update(self,  **kwargs):
        pass
