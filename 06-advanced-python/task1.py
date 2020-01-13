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
            print("")
            self.nodes = []
            self.unvisited = deque([v for v in E])
            raise StopIteration
        current = self.unvisited.popleft()
        if current not in self.nodes:
            self.nodes.append(current)
            print(current, end=" ")
        for t in self.E[current]:
            if t not in self.nodes:
                print(t, end=" ")
                self.nodes.append(t)
        return self.__next__()


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}

graph = Graph(E)

for vertex in graph:
    print(vertex)

# G = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A', 'Z', 'X'], 'Z':[]}

# graph2 = Graph(G)

# for vertex in graph2:
#     print(vertex)
