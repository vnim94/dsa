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

    def test_insert_keeps_bst_balanced(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(1)
        bst.insert(2)
        bst.insert(2)

        self.assertEqual(bst.left.root, 0)
        self.assertEqual(bst.left.right.root, 1)
        self.assertEqual(bst.right.root, 2)
        self.assertEqual(bst.right.left.root, 2)

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

class test_remove_method(unittest.TestCase):

    def test_remove_value_at_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.remove(1)

        self.assertIsNone(bst.root)

    def test_remove_value_in_right_sub_tree(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        
        bst.remove(2)

        self.assertIsNone(bst.right)

    def test_remove_values_in_right_sub_trees_in_order(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        
        bst.remove(3)
        self.assertIsNone(bst.right.right)

        bst.remove(2)
        self.assertIsNone(bst.right)

    def test_remove_value_in_right_sub_trees(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        
        bst.remove(2)

        self.assertEqual(bst.right.root, 3)
        self.assertEqual(bst.right.right.root, 4)

    def test_remove_value_in_left_sub_tree(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)

        bst.remove(0)

        self.assertIsNone(bst.left)

    def test_remove_values_in_left_sub_trees_in_order(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(0)

        bst.remove(0)
        self.assertIsNone(bst.left.left)

        bst.remove(1)
        self.assertIsNone(bst.left)

    def test_remove_value_in_left_sub_trees(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(0)
        bst.insert(-1)

        bst.remove(1)

        self.assertEqual(bst.left.root,0)
        self.assertEqual(bst.left.left.root, -1)

    def test_remove_value_in_left_and_right_sub_trees(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(2)

        bst.remove(0)
        self.assertIsNone(bst.left)

        bst.remove(2)
        self.assertIsNone(bst.right)

    def test_remove_keeps_bst_balanced(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(-1)
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(3)

        bst.remove(0)
        self.assertEqual(bst.left.root, 1)

        bst.remove(3)
        self.assertEqual(bst.right.right.root, 3)

class test_min_method(unittest.TestCase):

    def test_min_returns_root_in_bst_with_only_one_value(self):
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.min(), 1)

    
    def test_min_returns_lowest_value_in_bst(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(-1)

        self.assertEqual(bst.min(), -1)

class test_max_method(unittest.TestCase):

    def test_max_returns_largest_value_in_bst(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)

        self.assertEqual(bst.max(), 3)

class test_height_method(unittest.TestCase):

    def test_height_returns_0_for_tree_with_root_only(self):
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.height(), 0)

    def test_height_returns_1_for_tree_with_one_left_sub_tree_only(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)

        self.assertEqual(bst.height(), 1)

    def test_height_returns_1_for_tree_with_left_and_right_sub_tree(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(2)

        self.assertEqual(bst.height(), 1)

    def test_height_returns_2_for_tree_with_1_left_subtree_and_2_right_subtrees(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(2)
        bst.insert(3)

    def test_height_returns_2_for_tree_with_2_left_subtree_and_1_right_subtrees(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        bst.insert(-1)
        bst.insert(3)

    def test_height_returns_max_height_of_bst(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)

        self.assertEqual(bst.height(), 2)

@unittest.skip
class test_to_string_method(unittest.TestCase):

    def test_print_root_value(self):
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.__str__(), 1)