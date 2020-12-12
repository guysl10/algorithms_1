from dataclasses import dataclass
from typing import List


@dataclass
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
    e: List[Edge]

    # TODO: create weight function...
    # def weight(self, edge: Edge):
    #     generate
