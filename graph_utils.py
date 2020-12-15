import itertools
import random
from typing import List, Tuple
import heapq

from graph import Edge, Graph, Node

WEIGHT_START_RANGE = 1
WEIGHT_END_RANGE = 10
NODES_SIZE_START_RANGE = 4
NODES_SIZE_END_RANGE = 6
INFINITY_VALUE = 999


def heap_insert(graph: Graph, root: Node) -> List[Node]:
    """Fill the heap with all the graph nodes after sorting them."""
    h = []
    children = get_children(root, graph)
    for child in children:
        heapq.heappush(h, get_children(root, graph))
    return h


def get_children(node: Node, graph: Graph, is_root: bool = False) -> List[
    Node]:
    """
    Get all nodes the given node share edge with.
    :param node: given node to search in all edges in graph.
    :param graph: graph to search edges given node involve in.
    :return: all edges given node is part of.
    """
    #TODO: split into 2 diffetent functions. 1st - get_children 2nd -
    # insert_root_children. Moreover, add mst list and remember to insert
    # root & his children.
    children = []
    for edge in graph.e:
        if node in (edge.node1, edge.node2) and not edge.visited:
            if node == edge.node1:
                if is_root:
                    edge.node2.father = node
                    edge.node2.key = edge.weight
                children.append(edge.node2)
            else:
                if is_root:
                    edge.node1.father = node
                    edge.node1.key = edge.weight
                children.append(edge.node1)
            if not is_root:
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
        if (node1, node2) in [(edge.node1, edge.node2), (edge.node2,
                                                         edge.node1)]:
            return edge.weight
    return -1


def prim(graph: Graph, root: Node, weighter: callable) -> List[Node]:
    """
    Prim's algorithm
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :param weighter: weight function of node.
    :return: NMT graph (after running prim's algorithm).
    """
    for node in graph.v:
        node.key = INFINITY_VALUE

    q = []
    last_node = None
    children = get_children(root, graph, True)
    for child in children:
        heapq.heappush(q, child)

    root.key = 0
    root.parent = None
    while q:
        u = heapq.heappop(q)
        u_children = get_children(u, graph)
        for v in u_children:
            w = weighter(graph, u, v)
            if w < v.key and v not in q:
                v.father = u
                v.key = w
                heapq.heappush(q, v)
                last_node = v
    return get_mst(last_node)


def generate_graph() -> Graph:
    """Generate new graph with random all nodes & edges."""
    num_of_nodes = random.randint(NODES_SIZE_START_RANGE, NODES_SIZE_END_RANGE)
    nodes = [Node(node_id) for node_id in range(num_of_nodes)]
    combinations = list(itertools.combinations(nodes, 2))
    edges = [Edge(first, second, random.randint(1, 10)) for first, second in
             combinations]

    for edge_index, edge in enumerate(edges):
        if edge_index % 2 == 0:
            edges.remove(edge)
    return Graph(nodes, edges)


def main():
    new_graph = generate_graph()
    print("##############################\nbefore:\n")
    print_graph(new_graph)
    a = prim(new_graph, random.choice(new_graph.v), weight)
    print("##############################\nafter:\n")
    print_graph(new_graph)
    print(a)


def print_graph(graph: Graph):
    print("nodes:")
    for node in graph.v:
        print(f"{node} %{node.key}  ~{node.father}")
    print("edges:")
    for edge in graph.e:
        print(f"{edge.node1} - {edge.node2}  %{edge.weight}")


def get_mst(last_node: Node) -> List[Node]:
    mst = []
    while last_node.father is not None:
        mst.append(last_node)
        last_node = last_node.father
    return mst

if __name__ == "__main__":
    main()
