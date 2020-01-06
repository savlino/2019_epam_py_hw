"""
class Graph defined to breadth-first iterate over graph, given as dictionary
"""
from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E
        self.nodes = []
        self.unvisited = deque([v for v in E])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.unvisited:
            raise StopIteration
        curr = self.unvisited.popleft()
        if curr not in self.nodes:
            self.nodes.append(curr)
        for t in self.E[curr]:
            if t not in self.nodes:
                self.nodes.append(t)
        if not self.unvisited:
            return self.nodes
        return self.__next__()


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
