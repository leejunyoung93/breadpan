
from be.pkg.usecase import IUsecaseOutputPort, IUsecaseInteractor

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

class ToDoOutputPort(IUsecaseOutputPort):
    def __init__(self, **kwargs):
        super(ToDoOutputPort,self).__init__(**kwargs)
        # To-Do: Do any operation additionally.


class ToDoCreateInteractor(IUsecaseInteractor):
    def operate(self):        
        # Get id from the controller's data. 
        task_id = self.data["task_id"]
        contents = self.data["contents"]

        # Store the data. 
        TODOS[task_id] = contents

        # Link to output port
        return ToDoOutputPort(task={task_id:TODOS[task_id]})


class ToDoReadInteractor(IUsecaseInteractor):
    def operate(self):
        id = self.data["to_do_id"]
        return ToDoOutputPort(self)


class ToDoDeleteInteractor(IUsecaseInteractor):
    def operate(self):
        id = self.data["to_do_id"]
        del TODOS[todo_id]
        return ToDoOutputPort(self)