#!/usr/bin/env python
import unittest

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from pkg.interface.todo import ToDoController

class TestTodoApp(unittest.TestCase):

    TodoCtrl = None

    def setUp(self):
        self.TodoCtrl = ToDoController()

    def tearDown(self):
        del self.TodoCtrl

    def test_create(self):
        pass


if __name__ == '__main__':
    unittest.main()
