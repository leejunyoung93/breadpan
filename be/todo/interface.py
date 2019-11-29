from breadpan.interface import IController, IPresenter
from breadpan.usecase import IUsecaseOutputPort, IUsecaseInteractor
from todo.usecase import ToDoCreateInteractor, ToDoReadInteractor, ToDoDeleteInteractor


class ToDoPresenter(IPresenter):
    pass

class ToDoController(IController):
    def create(self, todo_id, contents):
        i = ToDoCreateInteractor()
        i.input(todo_id=todo_id, contents=contents)
        return ToDoPresenter(i.operate())

    def read(self, todo_id):
        i = ToDoReadInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.operate())

    def delete(self, todo_id):
        i = ToDoDeleteInteractor()
        i.input(todo_id=todo_id)
        return ToDoPresenter(i.operate())

    def update(self,  **kwargs):
        pass
