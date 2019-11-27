#!/usr/bin/env python
import unittest
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
