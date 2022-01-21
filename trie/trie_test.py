import unittest
from trie import Trie

class test_insert(unittest.TestCase):
    
    def test_insert_adds_nodes_for_each_character(self):
        trie = Trie()

        trie.insert('test')

        t = trie.root.pointers.get('t')
        e = t.pointers.get('e')
        s = e.pointers.get('s')
        lastT = s.pointers.get('t')

        self.assertIsNotNone(t)
        self.assertEqual(t.data, 't')

        self.assertIsNotNone(e)
        self.assertEqual(e.data, 'e')

        self.assertIsNotNone(s)
        self.assertEqual(s.data, 's')

        self.assertIsNotNone(lastT)
        self.assertEqual(lastT.data, 't')

        self.assertTrue(lastT.end)

    def test_insert_multiple_strings(self):
        None

        