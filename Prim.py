import itertools
from dataclasses import dataclass
import random
from typing import List, Tuple
import heapq


@classmethod
class Node:
    id: int
    key: int = 0
    father = None


class Edge:
    def __init__(self, node1: Node, node2: Node, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __sub__(self, other):
        return self.weight - other.weight

    def __add__(self, other):
        return self.weight + other.weight

    def __mul__(self, other):
        return self.weight * other.weight


@dataclass
class Graph:
    V: List[Node]
    E: List[Edge]

    def weight(self, edge: Edge):
        generate


def heap_sort(edges: List[Edge]):
    """
    Heap Sort Algorithm
    :param edges:
    :return:
    """
    h = []
    for edge in edges:
        heapq.heappush(h, edge)

    return [heapq.heappop(h) for i in range(len(h))]


def get_children(node: Node, graph: Graph) -> List[Edge]:
    """

    :param node:
    :param graph:
    :return:
    """
    return [E for E in graph.E if node in E.node1]


def prim(graph: Graph, root: Node, weight: callable):
    """
    Prim's algorithm
    :param graph:
    :param root:
    :param weight:
    :return:
    """
    # Q = sorted(graph.E, key=lambda k: k.weight)

    Q = heap_sort(graph.E)

    root.key = 0
    root.parent = None

    while Q:
        min_node = heapq.heappop(Q)

        min_child = min(get_children(min_node, graph))
        min_child.father = min_child


def main():
    num_of_nodes = random.randint(5, 8)
    nodes = [Node(random.randint(1, 10)) for _ in range(num_of_nodes)]
    combinations = list(itertools.combinations(nodes, 2))
    edges = []
    for first, second in combinations:
        edges.append(Edge(first, second, ))

    for i, E in enumerate(edges):
        if i % 2 == 0:
            edges.remove(E)

    prim(Graph(nodes, edges), random.choice(nodes), weight_func)

if __name__ == "__main__":
    main()