
from pkg.usecase import IUsecaseInputPort, IUsecaseOutputPort, IUseCaseInteractor
from pkg.interface import IController, IPresentor


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


class ToDoCreateInteractor(IUseCaseInteractor):
    def operate(self):
        id = self.data["to_do_id"]
        task = {'task': args['task']}
        TODOS[id] = task
        return IPresentor.output(task)


class ToDoReadInteractor(IUseCaseInteractor):
    def operate(self):
        id = self.data["to_do_id"]
        return IPresentor.output(TODOS[id])


class ToDoDeleteInteractor(IUseCaseInteractor):
    def operate(self):
        id = self.data["to_do_id"]
        del TODOS[todo_id]
        return IPresentor.output('')
