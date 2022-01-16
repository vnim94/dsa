import unittest
from trie import Trie

class test_insert(unittest.TestCase):
    
    def test_insert_adds_key(self):
        trie = Trie()

        trie.insert('that')

        self.assertEqual(trie.root.data, 't')
        


        