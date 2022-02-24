import unittest
from hash_table import HashTable


class test_initialise(unittest.TestCase):

    def test_initialise(self):
        table = HashTable()

        self.assertEqual(len(table.array), 10)

class test_hash_function(unittest.TestCase):
    
    def test_hash_returns_index(self):
        table = HashTable()
        index = table.hash('abc')

        self.assertTrue(10 >= 0 and index <= 10)

    def test_hash_returns_same_value_every_time(self):
        table = HashTable()
        index = table.hash('abcd')
        same = True

        for i in range(50):
            value = table.hash('abcd')
            if value != index:
                same = False

        self.assertTrue(same)
            
class test_put_method(unittest.TestCase):

    def test_put_adds_value_to_array_at_hashed_index(self):
        table = HashTable()
        index = table.hash('apple')

        table.put('apple', 1)

        storedValue = table.array[index].data[1]

        self.assertEqual(storedValue, 1)

class test_get_method(unittest.TestCase):

    def test_get_returns_value_for_key(self):
        table = HashTable()
        table.put('apple', 1)

        value = table.get('apple')

        self.assertEqual(value, 1)

class test_remove_method(unittest.TestCase):

    def test_remove_deletes_key_and_value(self):
        table = HashTable()
        table.put('apple', 1)

        table.remove('apple')

        value = table.get('apple')

        self.assertIsNone(value)

class test_chaining(unittest.TestCase):

    def test_put_chains_value_where_index_already_taken(self):
        table = HashTable()
        table.put('apple', 1)
        indexA = table.hash('apple')
        indexB = table.hash('pear')
        indexC = table.hash('abcd')

        self.assertEqual(indexA, indexB)
        self.assertEqual(indexB, indexC)

        table.put('pear', 2)
        table.put('abcd', 3)

        self.assertEqual(table.array[indexA].data[1], 3)

    def test_get_value_in_a_chain(self):
        table = HashTable()
        table.put('apple', 1)
        table.put('pear', 2)
        table.put('abcd', 3)

        value = table.get('apple')

        self.assertEqual(value, 1)

