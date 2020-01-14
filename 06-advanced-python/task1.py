"""
class Graph defined to breadth-first iterate over graph, given as dictionary
"""
from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        self.nodes = deque()
        self.unvisited = deque([v for v in self.E])
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if not self.unvisited:
            if self.i >= len(self.nodes):
                raise StopIteration
            else:
                return self.nodes[self.i]
                return
        current = self.unvisited.popleft()
        
        if current not in self.nodes:
            self.nodes.append(current)

        for t in self.E[current]:
            if t not in self.nodes:
                self.nodes.append(t)

        return self.nodes[self.i]

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}

graph = Graph(E)

for vertex in graph:
    print(vertex)

G = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A', 'Z', 'X'], 'Z':[]}

graph2 = Graph(G)

gr_iter = iter(graph2)

print(next(gr_iter))
print(next(gr_iter))
print(next(gr_iter))
print(next(gr_iter))
print(next(gr_iter))
print(next(gr_iter))
print(next(gr_iter))
