import unittest
from binary_search_tree import Node, BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
    
    def test_initialise(self):
        bst = BinarySearchTree()

        self.assertIsNone(bst.root)

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(0, 1)

        self.assertEqual(bst.root.data, 1)
        
    @unittest.skip
    def test_insert_value_greater_than_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertEqual(bst.root.data, 1)
        self.assertEqual(bst.root.right.data, 2)

    @unittest.skip
    def test_insert_value_less_than_root(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)

        self.assertEqual(bst.root.data, 2)
        self.assertEqual(bst.root.left.data, 1)

    @unittest.skip
    def test_insert_multiple_values(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.root.data, 2)
        self.assertEqual(bst.root.left.data, 1)
        self.assertEqual(bst.root.right.data, 3)

    @unittest.skip
    def test_insert_multiple_values_greater_than_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)

        self.assertEqual(bst.root.data, 1)
        self.assertEqual(bst.root.right.data, 2)
        self.assertEqual(bst.root.right.data, 3)

    @unittest.skip
    def test_insert_multiple_values_less_than_root(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(0)

        self.assertEqual(bst.root.data, 2)
        self.assertEqual(bst.root.left.data, 1)
        self.assertEqual(bst.root.left.left.data,0)
