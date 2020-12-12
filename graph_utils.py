import itertools
import random
from typing import List
import heapq

from graph import Edge, Graph, Node

WEIGHT_START_RANGE = 1
WEIGHT_END_RANGE = 10
NODES_SIZE_START_RANGE = 5
NODES_SIZE_END_RANGE = 8


def heap_sort(edges: List[Edge]) -> List[Edge]:
    """
    Heap Sort Algorithm on all edges.
    :param edges: edges to sort.
    :return: sorted edges.
    """
    h = []
    for edge in edges:
        heapq.heappush(h, edge)

    return [heapq.heappop(h) for i in range(len(h))]


def get_children(node: Node, graph: Graph) -> List[Edge]:
    """
    Get all edges the given node is part of.
    :param node: given node to search in all edges in graph.
    :param graph: graph to search edges given node involve in.
    :return: all edges given node is part of.
    """
    return [edge for edge in graph.e
            if node in edge.node1 or node in edge.node2]


def weight(graph: Graph, edge_index: int) -> int:
    """
    Calculate the weight of given edge index. if already exist just return
    the weight value.
    :param graph: given graph
    :param edge_index: given edge index for list in graph.
    :return: weight of needed edge.
    """
    if graph.e[edge_index].weight == 0:
        graph.e[edge_index].weight = random.randint(WEIGHT_START_RANGE,
                                                    WEIGHT_END_RANGE)
    return graph.e[edge_index].weight


def prim(graph: Graph, root: Node, weight: callable):
    """
    Prim's algorithm
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :param weight: weight function of node.
    :return: NMT graph (after running prim's algorithm).
    """
    # Q = sorted(graph.E, key=lambda k: k.weight)
    q = heap_sort(graph.e)

    root.key = 0
    root.parent = None

    while q:
        min_node = heapq.heappop(q)

        min_child = min(get_children(min_node, graph))
        min_child.father = min_child


def generate_graph() -> Graph:
    """Generate new graph with random all nodes & edges."""
    num_of_nodes = random.randint(NODES_SIZE_START_RANGE, NODES_SIZE_END_RANGE)
    nodes = [Node(random.randint(1, 10)) for _ in range(num_of_nodes)]
    combinations = list(itertools.combinations(nodes, 2))
    edges = [Edge(first, second, ) for first, second in combinations]

    for edge_index, edge in enumerate(edges):
        if edge_index % 2 == 0:
            edges.remove(edge)
    return Graph(nodes, edges)


def main():
    new_graph = generate_graph()
    prim(new_graph, random.choice(new_graph.v), weight)


if __name__ == "__main__":
    main()
