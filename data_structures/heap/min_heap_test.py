import unittest
from min_heap import Heap

class HeapTest(unittest.TestCase):

    def test_insert_adds_value_to_heap(self):
        heap = Heap()

        heap.insert(1)

        self.assertEqual(heap.nodes[0], 1)

    def test_insert_adds_value_to_correct_position(self):
        heap = Heap()

        heap.insert(2)
        heap.insert(1)
        heap.insert(0)

        self.assertEqual(heap.nodes[0], 0)
        self.assertEqual(heap.nodes[1], 2)
        self.assertEqual(heap.nodes[2], 1)

    def test_delete_replaces_root_with_new_min_and_removes_last_value(self):
        heap = Heap()

        heap.insert(2)
        heap.insert(1)
        heap.insert(0)

        heap.delete()

        self.assertEqual(heap.nodes[0], 1)
        self.assertEqual(heap.nodes[1], 2)
        self.assertEqual(len(heap.nodes), 2)

    def test_delete_replaces_root_with_new_min(self):
        heap = Heap()

        heap.insert(0)
        heap.insert(2)
        heap.insert(3)
        heap.insert(4)
        heap.insert(1)
        heap.insert(5)

        heap.delete()

        self.assertEqual(len(heap.nodes), 5)
        self.assertEqual(heap.nodes[0], 1)
        self.assertEqual(heap.nodes[1], 2)
        self.assertEqual(heap.nodes[2], 3)
        self.assertEqual(heap.nodes[3], 4)
        self.assertEqual(heap.nodes[4], 5)

