import unittest
from __graph import DirectedGraph, UndirectedGraph

class Test_DirectedGraph(unittest.TestCase):

    def test_insert_adds_node_to_graph(self):
        graph = DirectedGraph()

        graph.insert('A')

        self.assertTrue('A' in graph.nodes.keys())
        self.assertEqual(graph.nodes.get('A'), [])

    def test_link_links_nodeA_to_nodeB(self):
        graph = DirectedGraph()
        graph.insert('A')
        graph.insert('B')

        graph.link('A','B')

        self.assertTrue('B' in graph.nodes['A'])

    def test_contains_return_true_if_value_exists_in_graph(self):
        graph = DirectedGraph()
        graph.insert('A')

        self.assertTrue(graph.contains('A'))

    def test_depth_traverse_empty_graph(self):
        graph = DirectedGraph()

        self.assertEqual(graph.dfs('a'), [])

    def test_depth_traversal(self):
        graph = DirectedGraph()
        graph.insert('a','b','c','d','e','f')
        graph.link('a','c')
        graph.link('a','b')
        graph.link('c','e')
        graph.link('b','d')
        graph.link('d','f')
        
        dfs = graph.dfs('a')

        self.assertEqual(dfs, ['a','b','d','f','c','e'])

    def test_breadth_traversal(self):
        graph = DirectedGraph()
        graph.insert('a','b','c','d','e','f')
        graph.link('a','c')
        graph.link('a','b')
        graph.link('c','e')
        graph.link('b','d')
        graph.link('d','f')

        bfs = graph.bfs('a')

        self.assertEqual(bfs, ['a','c','b','e','d','f'])

    def test_hasPath_returns_true_if_path_exists(self):
        graph = DirectedGraph()
        graph.insert('f','g','h','i','j','k')
        graph.link('f','g')
        graph.link('f','i')
        graph.link('g','h')
        graph.link('i','g')
        graph.link('i','k')
        graph.link('j','i')

        self.assertTrue(graph.hasPath('j','h'))

    def test_hasPath_returns_false_if_path_does_not_exist(self):
        graph = DirectedGraph()
        graph.insert('f','g','h','i','j','k')
        graph.link('f','g')
        graph.link('f','i')
        graph.link('g','h')
        graph.link('i','g')
        graph.link('i','k')
        graph.link('j','i')

        self.assertFalse(graph.hasPath('k','h'))

    def test_toString_returns_object(self):
        graph = DirectedGraph()
        graph.insert('A')
        graph.insert('B')
        graph.link('A','B')

        output = {
            'A': ['B'],
            'B': []
        }

        self.assertEqual(graph.toString(), output)

class Test_UndirectedGraph(unittest.TestCase):

    def test_insert_adds_node_to_graph(self):
        graph = UndirectedGraph()

        graph.insert('A')

        self.assertTrue('A' in graph.nodes.keys())
        self.assertEqual(graph.nodes.get('A'), [])

    def test_link_links_nodeA_to_nodeB(self):
        graph = UndirectedGraph()
        graph.insert('A')
        graph.insert('B')

        graph.link('A','B')

        self.assertTrue('B' in graph.nodes['A'])
        self.assertTrue('A' in graph.nodes['B'])

    def test_contains_return_true_if_value_exists_in_graph(self):
        graph = UndirectedGraph()
        graph.insert('A')

        self.assertTrue(graph.contains('A'))

    def test_depth_traverse_empty_graph(self):
        graph = UndirectedGraph()

        self.assertEqual(graph.dfs('a'), [])

    def test_depth_traversal(self):
        graph = UndirectedGraph()
        graph.insert('a','b','c','d','e','f')
        graph.link('a','c')
        graph.link('a','b')
        graph.link('c','e')
        graph.link('b','d')
        graph.link('d','f')
        
        dfs = graph.dfs('a')

        self.assertEqual(dfs, ['a','b','d','f','c','e'])

    def test_breadth_traversal(self):
        graph = UndirectedGraph()
        graph.insert('a','b','c','d','e','f')
        graph.link('a','c')
        graph.link('a','b')
        graph.link('c','e')
        graph.link('b','d')
        graph.link('d','f')

        bfs = graph.bfs('a')

        self.assertEqual(bfs, ['a','c','b','e','d','f'])

    def test_hasPath_returns_true_if_path_exists(self):
        graph = UndirectedGraph()
        graph.insert('f','g','h','i','j','k')
        graph.link('f','g')
        graph.link('f','i')
        graph.link('g','h')
        graph.link('i','g')
        graph.link('i','k')
        graph.link('j','i')

        self.assertTrue(graph.hasPath('j','h'))

    def test_hasPath_returns_false_if_path_does_not_exist(self):
        graph = UndirectedGraph()
        graph.insert('i','j','k','l','m','o','n')
        graph.link('i','k')
        graph.link('i','j')
        graph.link('k','l')
        graph.link('k','m')
        graph.link('o','n')

        self.assertTrue(graph.hasPath('i','l'))
        self.assertFalse(graph.hasPath('i','n'))

    def test_toString_returns_object(self):
        graph = UndirectedGraph()
        graph.insert('A')
        graph.insert('B')
        graph.link('A','B')

        output = {
            'A': ['B'],
            'B': ['A']
        }

        self.assertEqual(graph.toString(), output)