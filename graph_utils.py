import itertools
import random
from typing import List, Tuple
import heapq

from graph import Edge, Graph, Node

WEIGHT_START_RANGE = 1
WEIGHT_END_RANGE = 10
NODES_SIZE_START_RANGE = 5
NODES_SIZE_END_RANGE = 8
INFINITY_VALUE = 999


def heap_sort(graph: Graph, root: Node) -> List[Node]:
    """
    Heap Sort Algorithm on all edges.
    :param graph: edges to sort.
    :param root: starting point of the heap.
    :return: sorted edges.
    """
    h = []


def heap_insert(graph: Graph, root: Node) -> List[Node]:
    """Fill the heap with all the graph nodes after sorting them."""
    h = []
    children = get_children(root, graph)
    for child in children:
        heapq.heappush(h, get_children(root, graph))
    return h


def get_children(node: Node, graph: Graph) -> List[Node]:
    """
    Get all nodes the given node share edge with.
    :param node: given node to search in all edges in graph.
    :param graph: graph to search edges given node involve in.
    :return: all edges given node is part of.
    """
    children = []
    for edge in graph.e:
        if node in (edge.node1, edge.node1) and not edge.visited:
            if node == edge.node1:
                edge.node2.key = edge.weight
                children.append(edge.node2)
            else:
                edge.node1.key = edge.weight
                children.append(edge.node1)
        edge.visited = True
    return children


def weight(graph: Graph, node1: Node, node2: Node) -> int:
    """
    Calculate the weight of given edge index. if already exist just return
    the weight value.
    :param node2:
    :param node1:
    :param graph: given graph
    :return: weight of needed edge.
    """
    for edge in graph.e:
        if (node1, node2) in [(edge.node1, edge.node2),(edge.node2,
                                                        edge.node1)]
            return edge.weight
    return -1


def prim(graph: Graph, root: Node, weight: callable):
    """
    Prim's algorithm
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :param weight: weight function of node.
    :return: NMT graph (after running prim's algorithm).
    """
    for node in graph.v:
        node.key = INFINITY_VALUE

    q = heap_insert(graph, root))

    root.key = 0
    root.parent = None

    while q:
        u = heapq.heappop(q)
        for v in get_children(u, graph):
            w = weight(u, v)
            if w < u.key:
                v.father = u
                v.key = w


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
    #prim(new_graph, random.choice(new_graph.v), weight)
    heap_insert(new_graph, new_graph.v[0], [])

    print(new_graph)


if __name__ == "__main__":
    main()
