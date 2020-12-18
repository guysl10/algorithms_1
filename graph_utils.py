import heapq
import itertools
import random
from typing import List, Tuple
from graph import Edge, Graph, Node

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
    # TODO: split into 2 different functions. 1st - get_children 2nd -
    # insert_root_children. Moreover, add mst list and remember to insert
    # root & his children.
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


def initial_prim(graph: Graph, root: Node) -> List[Node]:
    """
    Initial variables for Prim's algorithm.
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :return: The Q for prim's algorithm.
    """
    for node in graph.v:
        node.key = INFINITY_VALUE
    q = []
    children, _ = get_children(root, graph, True)
    for child in children:
        heapq.heappush(q, child)

    root.key = 0
    root.parent = None
    return q


def prim(graph: Graph, root: Node, get_weight: callable) -> List[Tuple[int,
                                                                       int,
                                                                       int]]:
    """
    Prim's algorithm.
    :param graph: given graph to run prim's algorithm on.
    :param root: starting node of prim's algorithm.
    :param get_weight: weight function of node.
    :return: NMT graph (after running prim's algorithm).
    """
    q = initial_prim(graph, root)
    mst = [(edge.node1.id, edge.node2.id, edge.weight) for edge in graph.e
           if root in (edge.node1, edge.node2)]
    while q:
        u = heapq.heappop(q)
        u_children, u_edges = get_children(u, graph)
        for v in u_children:
            w = get_weight(graph, u, v)
            if w < v.key and v not in q:
                v.father = u
                v.key = w
                heapq.heappush(q, v)

                mst.append((u.id, v.id, v.key))
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
    print("nodes:")
    for node in graph.v:
        print(f"{node} %{node.key}  ~{node.father}")
    print("edges:")
    for edge in graph.e:
        print(f"{edge.node1} - {edge.node2}  %{edge.weight}")


def print_mst(mst: List[Tuple[int, int, int]]):
    print("edges:")
    for edge_details in mst:
        print(f"|{edge_details[0]}-{edge_details[1]} weight"
              f"={edge_details[2]}|", end='')


def inset_new_edge(graph: Graph, mst: List[Node], new_edge: Edge):
    # TODO: ALOSH will continue tomorrow.
    mst.append(new_edge)
    ...


def main():
    new_graph = generate_graph()
    print("##############################\nbefore:\n")
    print_graph(new_graph)
    mst = prim(new_graph, random.choice(new_graph.v), weight)
    print("##############################\nafter:\n")
    print_graph(new_graph)
    print_mst(mst)


if __name__ == "__main__":
    main()
