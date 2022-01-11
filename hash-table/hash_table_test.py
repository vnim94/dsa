import unittest
from hash_table import HashTable


class test_initialise(unittest.TestCase):

    def test_initialise(self):
        map = HashTable()

        self.assertEqual(len(map.array), 10)

class test_hash_function(unittest.TestCase):
    
    def test_hash_returns_index(self):
        map = HashTable()
        index = map.hash('abc')

        self.assertTrue(10 >= 0 and index <= 10)

    def test_hash_returns_same_value_every_time(self):
        map = HashTable()
        index = map.hash('abcd')
        same = True

        for i in range(50):
            value = map.hash('abcd')
            if value != index:
                same = False

        self.assertTrue(same)
            
class test_put_method(unittest.TestCase):

    def test_put_adds_value_to_array_at_hashed_index(self):
        map = HashTable()
        index = map.hash('apple')

        map.put('apple', 1)

        storedValue = map.array[index]

        self.assertEqual(storedValue, 1)

class test_get_method(unittest.TestCase):

    def test_get_returns_value_for_key(self):
        map = HashTable()
        map.put('apple', 1)

        value = map.get('apple')

        self.assertEqual(value, 1)

class test_remove_method(unittest.TestCase):

    def test_remove_deletes_key_and_value(self):
        map = HashTable()
        map.put('apple', 1)

        map.remove('apple')

        value = map.get('apple')

        self.assertIsNone(value)