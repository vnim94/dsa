import unittest
from __graph import Graph

class TestGraph(unittest.TestCase):

    def test_insert_adds_node_to_graph(self):
        graph = Graph()

        graph.insert('A')

        self.assertTrue('A' in graph.nodes.keys())
        self.assertEqual(graph.nodes.get('A'), [])

    def test_link_links_nodeA_to_nodeB(self):
        graph = Graph()
        graph.insert('A')
        graph.insert('B')

        graph.link('A','B')

        self.assertTrue('B' in graph.nodes['A'])

    def test_contains_return_true_if_value_exists_in_graph(self):
        graph = Graph()
        graph.insert('A')

        self.assertTrue(graph.contains('A'))

    def test_depth_traverse_empty_graph(self):
        graph = Graph()

        self.assertEqual(graph.traverseDepth(), [])

    def test_depth_traversal(self):
        graph = Graph()
        graph.insert('a','b','c','d','e','f')
        graph.link('a','b')
        graph.link('a','c')
        graph.link('b','d')
        graph.link('c','e')
        graph.link('d','f')
        graph.link('e','b')
        
        dfs = graph.traverseDepth()

        self.assertEqual(dfs, ['a','b','d','c','e','f'])

    def test_toString_returns_object(self):
        graph = Graph()
        graph.insert('A')
        graph.insert('B')
        graph.link('A','B')

        output = {
            'A': ['B'],
            'B': ['A']
        }

        self.assertEqual(graph.toString(), output)
