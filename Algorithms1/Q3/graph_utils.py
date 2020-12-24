"""

NAME: Alex Troitsky
ID: 321245813

NAME: Guy Salomon
ID: 316443845

"""
import heapq
import itertools
import random
from typing import List, Tuple

from Algorithms1.Q3.graph import Graph, Edge, Node

WEIGHT_START_RANGE = 1
WEIGHT_END_RANGE = 30
NODES_SIZE_START_RANGE = 20
NODES_SIZE_END_RANGE = 50
INFINITY_VALUE = 999

MAX_EDGE_RANGE = 70
MIN_EDGE_RANGE = 50


def get_children(node: Node, graph: Graph,
                 is_root: bool = False) -> Tuple[List[Node], List[Edge]]:
    """
    Get all nodes the given node share edge with.
    :param is_root:
    :param node: given node to search in all edges in graph.
    :param graph: graph to search edges given node involve in.
    :return: all edges given node is part of.
    """
    children = []
    children_edges = []
    for edge in graph.e:
        if node in (edge.node1, edge.node2) and not edge.visited:
            child = [n for n in (edge.node1, edge.node2) if n != node][0]
            if is_root:
                child.father = node
                child.key = edge.weight
            else:
                edge.visited = True
            children.append(child)
            children_edges.append(edge)
    return children, children_edges


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


def initial_prim(graph: Graph,
                 root: Node) -> Tuple[list, Graph]:
    """
    Initial variables for Prim's algorithm.
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :return: The Q for prim's algorithm.
    """
    for node in graph.v:
        node.key = INFINITY_VALUE
    q = []
    children, root_edges = get_children(root, graph, True)
    for child in children:
        heapq.heappush(q, child)

    root.key = 0
    root.parent = None
    children.insert(0, root)
    return q, Graph(children, root_edges)


def prim(graph: Graph, root: Node,
         get_weight: callable) -> Graph:
    """
    Prim's algorithm.
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :param get_weight: weight function of node.
    :return: NMT graph (after running prim's algorithm).
    """
    q, mst = initial_prim(graph, root)

    while q:
        u = heapq.heappop(q)
        u_children, u_edges = get_children(u, graph)
        for v in u_children:
            w = get_weight(graph, u, v)
            if w < v.key and v not in q:
                v.father = u
                v.key = w
                heapq.heappush(q, v)
                mst.e.append(Edge(u, v, v.key))
                mst.v.append(v)
    return mst


def generate_graph() -> Graph:
    """Generate new graph with random all nodes & edges."""
    num_of_nodes = random.randint(NODES_SIZE_START_RANGE, NODES_SIZE_END_RANGE)
    nodes = [Node(node_id) for node_id in range(num_of_nodes)]
    combinations = list(itertools.combinations(nodes, 2))
    edges = [Edge(first, second, random.randint(MIN_EDGE_RANGE, MAX_EDGE_RANGE)) for first, second in
             combinations]

    for edge_index, edge in enumerate(edges):
        if edge_index % 2 == 0:
            edges.remove(edge)
    return Graph(nodes, edges)


def get_mst(last_node: Node) -> List[Node]:
    mst = []
    while last_node.father is not None:
        mst.append(last_node)
        last_node = last_node.father
    return mst


def print_graph(graph: Graph):
    print("# Nodes:")
    for node in graph.v:
        print(f"{node.id} Weight={node.key}  Father={node.father}")
    print("# Edges:")
    for edge in graph.e:
        print(f"{edge.node1.id}<->{edge.node2.id}  Weight={edge.weight}")


def inset_new_edge(graph: Graph, new_edge: Edge):
    """
    inserting new edge to the mst graph and change the graph accordingly
    :param graph: mst graph
    :param new_edge: an edge to add to the mst graph
    """
    graph.e.append(new_edge)
    graph.remove_edge(find_heaviest_edge(new_edge))

    print(f"##############################\nafter adding edge: {new_edge.node1}, {new_edge.node2}, {new_edge.weight}\n")
    print_graph(graph)


def find_heaviest_edge(new_edge: Edge) -> Edge:
    """
    find the heaviest edge in the cycle to remove it later, maximum time O(n)
    :param new_edge: the edge to add to the mst graph
    :return: return the heaviest edge in the cycle
    """
    node1_pointer = new_edge.node1
    node2_pointer = new_edge.node2
    heaviest_edge = new_edge

    while node1_pointer != node2_pointer:
        if node1_pointer.father:
            temp_edge = Edge(node1_pointer, node1_pointer.father, node1_pointer.key)
            if temp_edge > heaviest_edge:
                heaviest_edge = temp_edge
            node1_pointer = node1_pointer.father

        if node2_pointer.father:
            temp_edge = Edge(node2_pointer, node2_pointer.father, node2_pointer.key)
            if temp_edge > heaviest_edge:
                heaviest_edge = temp_edge
            node2_pointer = node2_pointer.father if node2_pointer.father else node2_pointer

    return heaviest_edge


def main():
    new_graph = generate_graph()
    print("##############################\nbefore:\n")
    print_graph(new_graph)
    root = random.choice(new_graph.v)
    mst = prim(new_graph, root, weight)
    print("##############################\nafter mst:\n")

    print_graph(mst)
    print("Adding an edge that doesn't change MST")
    inset_new_edge(mst, Edge(mst.v[-1], root, WEIGHT_END_RANGE))

    print("Adding an edge that changes MST")
    inset_new_edge(mst, Edge(mst.v[-1], root, WEIGHT_START_RANGE))

if __name__ == "__main__":
    main()
