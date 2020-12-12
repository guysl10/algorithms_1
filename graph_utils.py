import itertools
import random
from typing import List
import heapq

from graph import Edge, Graph, Node


def heap_sort(edges: List[Edge]) -> List[Edge]:
    """
    Heap Sort Algorithm
    :param edges:
    :return
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
    return [E for E in graph.e if node in E.node1]


def prim(graph: Graph, root: Node, weight: callable):
    """
    Prim's algorithm
    :param graph:
    :param root:
    :param weight:
    :return:
    """
    # Q = sorted(graph.E, key=lambda k: k.weight)
    q = heap_sort(graph.e)

    root.key = 0
    root.parent = None

    while q:
        min_node = heapq.heappop(q)

        min_child = min(get_children(min_node, graph))
        min_child.father = min_child


def main():
    num_of_nodes = random.randint(5, 8)
    nodes = [Node(random.randint(1, 10)) for _ in range(num_of_nodes)]
    combinations = list(itertools.combinations(nodes, 2))
    edges = []
    for first, second in combinations:
        edges.append(Edge(first, second, ))

    for i, e in enumerate(edges):
        if i % 2 == 0:
            edges.remove(e)

    prim(Graph(nodes, edges), random.choice(nodes), weight_func)


if __name__ == "__main__":
    main()
