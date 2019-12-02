#!/usr/bin/env python
from .context import todo
import unittest

class TestTodoApp(unittest.TestCase):

    todo_ctrl = None

    def setUp(self):
        self.todo_ctrl = todo.ToDoController()

    def tearDown(self):
        del self.todo_ctrl

    def test_create(self):
        todo_id = "task312"
        contents = {'task': 'myid'}
        output = self.todo_ctrl.create(todo_id, contents)
        t = output.data["todo"]
        self.assertEqual(t ,{todo_id:contents} )

    def test_read(self):        
        output = self.todo_ctrl.read(todo_id='todo1')
        t = output.data["todo"]
        self.assertEqual(t,  {'todo1': {'task': 'build an API'} } )


    def test_read_all(self):        
        output = self.todo_ctrl.read_all_data()
        self.assertNotEqual( len(output.data["todo"]), 0)

    def test_update(self):
        todo_id = "task312"
        contents = {'task': 'myid'}
        self.todo_ctrl.create(todo_id, contents)
        new_contents = {'task': 'read the books'}
        self.todo_ctrl.update(todo_id, new_contents)    

        output = self.todo_ctrl.read(todo_id)
        t = output.data["todo"]
        self.assertEqual(t[todo_id]['task'] ,'read the books' )


    def test_delete(self):
        self.todo_ctrl.delete(todo_id='todo2')
        try:
            output = self.todo_ctrl.read(todo_id='todo2')
        except:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
