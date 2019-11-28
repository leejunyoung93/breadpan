#!/usr/bin/env python
import unittest

# Add parent path to import pkg modules. 
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
        
        task_id = "task312"
        contents = "New work"
        output = self.TodoCtrl.create(task_id, contents)

        t = output.data["task"]
        self.assertEqual( t , {task_id:contents} )
        



if __name__ == '__main__':
    unittest.main()
