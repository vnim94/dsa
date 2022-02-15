import unittest
from deque import Deque

class DequeTest(unittest.TestCase):

    def test_addLast_adds_value_to_back_of_queue(self):
        deque = Deque()
        deque.addLast(1, 2, 3)

        self.assertEqual(deque.front.data, 1)
        self.assertEqual(deque.back.data, 3)
        self.assertEqual(deque.length, 3)

    def test_addFirst_adds_value_to_front_of_queue(self):
        deque = Deque()
        deque.addFirst(3, 2, 1)

        self.assertEqual(deque.front.data, 1)
        self.assertEqual(deque.back.data, 3)
        self.assertEqual(deque.length, 3)
    
    def test_removeFirst_removes_and_returns_value_from_front_of_queue(self):
        deque = Deque()
        deque.addLast(1, 2, 3)
        first = deque.removeFirst()

        self.assertEqual(first, 1)
        self.assertEqual(deque.front.data, 2)

    def test_removeLast_removes_and_returns_value_from_back_of_queue(self):
        deque = Deque()
        deque.addLast(1, 2, 3)
        last = deque.removeLast()

        self.assertEqual(last, 3)
        self.assertEqual(deque.back.data, 2)
