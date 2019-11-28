#!/usr/bin/env python
import unittest

# Add parent path to import back-end pkg modules. 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from be.pkg.interface.todo import ToDoController

class TestTodoApp(unittest.TestCase):

    TodoCtrl = None

    def setUp(self):
        self.TodoCtrl = ToDoController()

    def tearDown(self):
        del self.TodoCtrl

    def test_create(self):
        todo_id = "task312"
        contents = {'task': 'myid'}
        output = self.TodoCtrl.create(todo_id, contents)
        t = output.data["todo"]
        self.assertEqual( t , {todo_id:contents} )

    def test_read(self):        
        output = self.TodoCtrl.read(task_id='todo1')
        t = output.data["todo"]
        self.assertEqual( t, { 'todo1': {'task': 'build an API'} } )
        

    def test_delete(self):
        pass    



if __name__ == '__main__':
    unittest.main()
