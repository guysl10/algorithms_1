import itertools
import random
from typing import List
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


def fill_heap(graph: Graph, root: Node, h: List[Node]) -> List[Node]:
    """Fill the heap with all the graph nodes after sorting them."""
    if root is None:
        return []

    if root not in h:
        heapq.heappush(h, root)
    children = sorted(get_children(root, graph))
    for child in children:
        for node in fill_heap(graph, child, h):
            heapq.heappush(h, node)


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
                children.append(edge.node2)
            else:
                children.append(edge.node1)
        edge.visited = True
    return children


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


# def prim(graph: Graph, root: Node, weight: callable):
#     """
#     Prim's algorithm
#     :param graph: given graph to run prim's algorithm on.
#     :param root: starting node of prim's algorithm.
#     :param weight: weight function of node.
#     :return: NMT graph (after running prim's algorithm).
#     """
#     for node in graph.v:
#         node.key = INFINITY_VALUE
#
#     q = heap_sort(graph.e, root)
#
#     root.key = 0
#     root.parent = None
#
#     while q:
#         min_edge = heapq.heappop(q)
#
#         min_child = min(get_children(min_edge, graph))
#
#         min_child.father = min_child


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
    print(new_graph)


if __name__ == "__main__":
    main()
