import unittest
import copy

import recursion.recursive_floyd as rec
import iterative.iterative_floyd as it

NO_PATH = float('inf')

# Base graph of the assignment
BASE_GRAPH = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]


class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        """Reset both graphs before each test"""
        rec.GRAPH = copy.deepcopy(BASE_GRAPH)
        it.GRAPH = copy.deepcopy(BASE_GRAPH)

    def test_iterative_runs(self):
        """Iterative version runs without crashing"""
        it.iterative_floyd()

    def test_recursive_runs(self):
        """Recursive version runs without crashing"""
        rec.recursive_floyd_warshall()

    def test_known_shortest_paths(self):
        """Check known shortest path values"""
        rec.recursive_floyd_warshall()

        self.assertEqual(rec.GRAPH[0][2], 12)  # 0 → 1 → 2
        self.assertEqual(rec.GRAPH[0][3], 8)   # direct is best
        self.assertEqual(rec.GRAPH[1][3], 7)   # 1 → 2 → 3

    def test_diagonal_zero(self):
        """Distance from node to itself should be 0"""
        rec.recursive_floyd_warshall()

        for i in range(len(rec.GRAPH)):
            self.assertEqual(rec.GRAPH[i][i], 0)

    def test_no_path_remains(self):
        """Unreachable nodes should stay NO_PATH"""
        rec.recursive_floyd_warshall()

        self.assertEqual(rec.GRAPH[1][0], NO_PATH)

    def test_recursive_vs_iterative(self):
        """Both implementations should produce identical results"""
        rec.recursive_floyd_warshall()
        result_recursive = copy.deepcopy(rec.GRAPH)

        it.iterative_floyd()
        result_iterative = copy.deepcopy(it.GRAPH)

        self.assertEqual(result_recursive, result_iterative)

    def test_single_node_graph(self):
        """Graph with one node"""
        rec.GRAPH = [[0]]
        it.GRAPH = [[0]]

        rec.recursive_floyd_warshall()
        it.iterative_floyd()

        self.assertEqual(rec.GRAPH, [[0]])
        self.assertEqual(it.GRAPH, [[0]])

    def test_disconnected_graph(self):
        """Graph where no nodes are connected"""
        graph = [
            [0, NO_PATH],
            [NO_PATH, 0]
        ]

        rec.GRAPH = copy.deepcopy(graph)
        it.GRAPH = copy.deepcopy(graph)

        rec.recursive_floyd_warshall()
        it.iterative_floyd()

        self.assertEqual(rec.GRAPH, graph)
        self.assertEqual(it.GRAPH, graph)

    def test_triangle_graph(self):
        """Test indirect path is shorter than direct"""
        graph = [
            [0, 10, 100],
            [NO_PATH, 0, 5],
            [NO_PATH, NO_PATH, 0]
        ]

        rec.GRAPH = copy.deepcopy(graph)

        rec.recursive_floyd_warshall()

        # 0 → 1 → 2 = 15 is shorter than direct 100
        self.assertEqual(rec.GRAPH[0][2], 15)

    def test_zero_weight_edges(self):
        """Graph with zero-weight edges"""
        graph = [
            [0, 0, NO_PATH],
            [NO_PATH, 0, 0],
            [NO_PATH, NO_PATH, 0]
        ]

        rec.GRAPH = copy.deepcopy(graph)
        rec.recursive_floyd_warshall()

        self.assertEqual(rec.GRAPH[0][2], 0)

    def test_already_optimal_graph(self):
        """Graph where all shortest paths are already optimal"""
        graph = [
            [0, 1],
            [NO_PATH, 0]
        ]

        rec.GRAPH = copy.deepcopy(graph)
        rec.recursive_floyd_warshall()

        self.assertEqual(rec.GRAPH, graph)


if __name__ == "__main__":
    unittest.main()