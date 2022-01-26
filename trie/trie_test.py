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

    def test_insert_overlapping_strings(self):
        trie = Trie()

        trie.insert('test')
        trie.insert('testing')

        t = trie.root.pointers.get('t')
        e = t.pointers.get('e')
        s = e.pointers.get('s')
        t2 = s.pointers.get('t')
        i = t2.pointers.get('i')
        n = i.pointers.get('n')
        g = n.pointers.get('g')

        self.assertIsNotNone(g)
        self.assertEqual(g.data, 'g')
        self.assertTrue(g.end)

    def test_insert_diverging_strings(self):
        trie = Trie()

        trie.insert('testing')
        trie.insert('tester')

        t = trie.root.pointers.get('t')
        e = t.pointers.get('e')
        s = e.pointers.get('s')
        t2 = s.pointers.get('t')
        i = t2.pointers.get('i')
        n = i.pointers.get('n')
        g = n.pointers.get('g')

        e2 = t2.pointers.get('e')
        r = e2.pointers.get('r')

        self.assertIsNotNone(g)
        self.assertEqual(g.data, 'g')
        self.assertTrue(g.end)

        self.assertIsNotNone(r)
        self.assertEqual(r.data, 'r')
        self.assertTrue(r.end)

class test_delete(unittest.TestCase):

    def test_delete_single_char_from_trie(self):
        trie = Trie()
        trie.insert('t')

        trie.delete('t')

        self.assertIsNone(trie.root.pointers.get('t'))

    def test_delete_string_from_trie(self):
        trie = Trie()
        trie.insert('test')

        trie.delete('test')

        self.assertIsNone(trie.root.pointers.get('t'))

class test_search(unittest.TestCase):

    def test_search_for_string(self):
        trie = Trie()
        trie.insert('test')

        self.assertTrue(trie.search('test'))

    def test_search_for_non_existent_string(self):
        trie = Trie()
        
        self.assertFalse(trie.search('test'))

    def test_search_for_string_with_multiple_strings_in_trie(self):
        trie = Trie()
        trie.insert('test')
        trie.insert('testing')

        self.assertTrue(trie.search('test'))
        self.assertTrue(trie.search('testing'))