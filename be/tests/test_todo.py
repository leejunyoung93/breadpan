#!/usr/bin/env python
from .context import todo
import unittest

class TestTodoApp(unittest.TestCase):

    TodoCtrl = None

    def setUp(self):
        self.TodoCtrl = todo.ToDoController()

    def tearDown(self):
        del self.TodoCtrl

    def test_create(self):
        todo_id = "task312"
        contents = {'task': 'myid'}
        output = self.TodoCtrl.create(todo_id, contents)
        t = output.data["todo"]
        self.assertEqual( t , {todo_id:contents} )

    def test_read(self):        
        output = self.TodoCtrl.read(todo_id='todo1')
        t = output.data["todo"]
        self.assertEqual( t, { 'todo1': {'task': 'build an API'} } )


    def test_delete(self):
        self.TodoCtrl.delete(todo_id='todo2')
        try:
            output = self.TodoCtrl.read(todo_id='todo2')
        except:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
