from dataclasses import dataclass
from random import random
from typing import List


@dataclass
class Node:
    id: int
    key: int = 0
    father = None


class Edge:
    def __init__(self, node1: Node, node2: Node):
        self.node1 = node1
        self.node2 = node2
        self.weight = 0

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
    """
    Represent a graph without directions.
    :ivar v: All nodes of graph.
    :ivar e: All edges of graph.
    """
    v: List[Node]
    e: List[Edge]



class Heap