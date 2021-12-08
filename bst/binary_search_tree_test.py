import unittest
from binary_search_tree import BinarySearchTree

class test_insert_method(unittest.TestCase):
    
    def test_initialise(self):
        bst = BinarySearchTree()

        self.assertIsNone(bst.root)

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.root, 1)

    def test_insert_value_greater_than_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertEqual(bst.root, 1)
        self.assertEqual(bst.right.root, 2)

    def test_insert_value_less_than_root(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)

        self.assertEqual(bst.root, 2)
        self.assertEqual(bst.left.root, 1)

    def test_insert_multiple_values(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.root, 2)
        self.assertEqual(bst.left.root, 1)
        self.assertEqual(bst.right.root, 3)

    def test_insert_multiple_values_greater_than_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)

        self.assertEqual(bst.root, 1)
        self.assertEqual(bst.right.root, 2)
        self.assertEqual(bst.right.right.root, 3)

    def test_insert_multiple_values_less_than_root(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(0)

        self.assertEqual(bst.root, 2)
        self.assertEqual(bst.left.root, 1)
        self.assertEqual(bst.left.left.root,0)

class test_search_method(unittest.TestCase):

    def test_search_for_value_at_root(self):
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertTrue(bst.search(1))

    def test_search_for_value_in_right_sub_tree(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertTrue(bst.search(2))

    def test_search_for_value_in_left_sub_tree(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)

        self.assertTrue(bst.search(1))

@unittest.skip
class test_to_string_method(unittest.TestCase):

    def test_print_root_value(self):
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.__str__(), 1)