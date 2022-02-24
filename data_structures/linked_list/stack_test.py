from stack import Stack, Node
import unittest

class StackTest(unittest.TestCase):

    def test_initialise(self):
        stack = Stack()
        self.assertTrue(stack.top.data == None)

    def test_push(self):
        stack = Stack()
        stack.push(1)

        self.assertEqual(stack.top.data, 1)

    def test_push_multiple_values(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.top.data, 3)
        self.assertEqual(stack.top.next.data, 2)
        self.assertEqual(stack.top.next.next.data, 1)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.pop()

        self.assertTrue(stack.top.data == None)

    def test_pop_value_from_multiple_values(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()

        self.assertEqual(stack.top.data, 2)
        self.assertEqual(stack.top.next.data, 1)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        top = stack.peek()

        self.assertEqual(top, 3)

    def test_isEmpty(self):
        stack = Stack()
        
        self.assertTrue(stack.isEmpty())

    def test_size(self):
        stack = Stack()
        
        self.assertEqual(stack.size(), 0)

    def test_size_on_stack_of_size_3(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.size(), 3)