
from queue import Queue, Node
import unittest

class QueueTest(unittest.TestCase):

    def test_initialise(self):
        queue = Queue()

        self.assertIsNone(queue.head.data)

    def test_add(self):
        queue = Queue()
        queue.add(1)

        self.assertEqual(queue.head.data, 1)

    def test_add_sets_tail_to_last_value(self):
        queue = Queue()
        queue.add(1)
        queue.add(2)

        self.assertEqual(queue.tail.data,2)

    def test_add_multiple_values(self):
        queue = Queue()
        queue.add(1)
        queue.add(2)
        queue.add(3)
        queue.add(4)

        self.assertEqual(queue.head.data, 1)
        self.assertEqual(queue.head.next.data, 2)
        self.assertEqual(queue.head.next.next.data, 3)
        self.assertEqual(queue.tail.data, 4)

    def test_remove(self):
        queue = Queue()
        queue.add(1)
        queue.remove()

        self.assertIsNone(queue.head.data)

    def test_remove_from_multiple_values(self):
        queue = Queue()
        queue.add(1)
        queue.add(2)
        queue.add(3)

        queue.remove()

        self.assertEqual(queue.head.data, 2)
        self.assertEqual(queue.tail.data, 3)

    def test_peek(self):
        queue = Queue()
        queue.add(1)

        self.assertEqual(queue.peek(),1)

    def test_poll(self):
        queue = Queue()
        queue.add(1)

        head = queue.poll()

        self.assertEqual(head, 1)
        self.assertIsNone(queue.head.data)

    def test_poll_on_queue_with_multiple_values(self):
        queue = Queue()
        queue.add(1)
        queue.add(2)

        head = queue.poll()

        self.assertEqual(head,1)
        self.assertEqual(queue.head.data,2)

    def test_size(self):   
        queue = Queue()
        queue.add(1)
        queue.add(2)
        queue.add(3)
        queue.add(4)

        self.assertEqual(queue.size(), 4)