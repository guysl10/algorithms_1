import heapq
import itertools
import random
from typing import List, Tuple

from Algorithms1.Q3.graph import Graph, Edge, Node

WEIGHT_START_RANGE = 1
WEIGHT_END_RANGE = 10
NODES_SIZE_START_RANGE = 4
NODES_SIZE_END_RANGE = 6
INFINITY_VALUE = 999


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
    edges = [Edge(first, second, random.randint(1, 10)) for first, second in
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
    graph.e.append(new_edge)
    cycles = []
    for node in graph.v:
        dfs_detect_cycle_undirected_graph(graph, node, cycles)


def dfs_detect_cycle_undirected_graph(graph: Graph, src: Node, cycle: List[Node]):
    """

    :param graph:
    :param src:
    :param cycle:
    :return:
    """
    graph.visited[src.id] = True

    for adj_node in get_children(src, graph)[0]:
        if not graph.visited[adj_node.id]:
            adj_node.father = src
            cycle.append(dfs_detect_cycle_undirected_graph(graph, adj_node, cycle))
        elif src.father != adj_node:
            # Already visited child but it's not the parent of our src (root) node
            print("Found a cycle in graph")
            return adj_node


def main():
    new_graph = generate_graph()
    print("##############################\nbefore:\n")
    print_graph(new_graph)
    mst = prim(new_graph, random.choice(new_graph.v), weight)
    print("##############################\nafter mst:\n")

    print_graph(mst)
    inset_new_edge(new_graph, Edge(new_graph.v[-1], new_graph.v[-2], 10))




if __name__ == "__main__":
    main()
