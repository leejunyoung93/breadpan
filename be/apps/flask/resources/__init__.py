""" Resource packages

- Represents the resource to expose via HTTP.
- This layer is outterrior of software depending on the framework.
- So implements the resource class for 
"""

from http import HTTPStatus

# Todo
# shows a single todo item and lets you delete a todo item


class FlaskTodoController(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id], HTTPStatus.OK

    def delete(self, todo_id):
        return '',  HTTPStatus.NO_CONTENT

    def put(self, todo_id):
        return task, HTTPStatus.CREATED


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class FlaskTodoListController(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], HTTPStatus.CREATED
