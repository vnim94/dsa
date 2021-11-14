from linked_list import LinkedList, Node
import unittest

class LinkedListTest(unittest.TestCase):

    def test_initialise(self):
        linkedList = LinkedList()
        
        self.assertIsNone(linkedList.head.data)

    def test_get(self):
        linkedList = LinkedList()
        linkedList.head.data = 1
        
        self.assertEqual(linkedList.get(0), 1)

    def test_get_element_after_head(self):
        linkedList = LinkedList()
        linkedList.head.next = Node(2)
        linkedList.head.next.next = Node(3)
        
        self.assertEqual(linkedList.get(2), 3)

    def test_contains_data_at_head(self):
        linkedList = LinkedList()
        linkedList.head.data = 1
        
        self.assertTrue(linkedList.contains(1))

    def test_contains_multiple_data_points(self):
        linkedList = LinkedList()
        linkedList.head.data = 1
        linkedList.head.next = Node(2)
        linkedList.head.next.next = Node(3)

        self.assertTrue(linkedList.contains(2))
        self.assertTrue(linkedList.contains(3))

    def test_add_inserts_value_at_head_of_empty_list(self):
        linkedList = LinkedList()
        linkedList.add(1)

        self.assertEqual(linkedList.head.data, 1)

    def test_add_inserts_value_at_end_of_list(self):
        linkedList = LinkedList()
        linkedList.head.data = 1
        linkedList.add(2)
        
        self.assertEqual(linkedList.get(1), 2)
        
    def test_insert_into_empty_list(self):
        linkedList = LinkedList()
        linkedList.insert(0,5)

        self.assertEqual(linkedList.get(0), 5)

    def test_insert_multiple_values(self):
        linkedList = LinkedList()
        linkedList.insert(0,5)
        linkedList.insert(0,6)
        linkedList.insert(0,7)
       
        self.assertEqual(linkedList.get(0),7)
        self.assertEqual(linkedList.get(1),6)
        self.assertEqual(linkedList.get(2),5)

    def test_set_updates_value_at_index(self):
        linkedList = LinkedList()
        linkedList.add(1)
        linkedList.add(2)
        
        linkedList.set(1,5)

        self.assertEqual(linkedList.get(1),5)

    def test_push_inserts_value_at_head(self):
        linkedList = LinkedList()
        linkedList.add(1)
        linkedList.add(2)

        linkedList.push(5)

        self.assertEqual(linkedList.get(0),5)

    def test_pop_removes_value_at_end_of_list(self):
        linkedList = LinkedList()
        linkedList.add(1)
        linkedList.add(2)

        linkedList.pop()

        self.assertEqual(linkedList.size(),1)

    def test_remove_value_at_index(self):
        linkedList = LinkedList()
        linkedList.add(1)
        linkedList.add(2)

        linkedList.remove(1)

        self.assertEqual(linkedList.size(), 1)

    def test_size_returns_length_of_list(self):
        linkedList = LinkedList()
        linkedList.add(1)
        linkedList.add(2)

        self.assertEqual(linkedList.size(),2)

    def test_print_string(self):
        linkedList = LinkedList()
        linkedList.head.data = 1
        linkedList.head.next = Node(2)
        linkedList.head.next.next = Node(3)
        string = linkedList.__str__()

        self.assertEqual(string, '1 -> 2 -> 3')
