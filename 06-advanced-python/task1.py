"""
class Graph defined to breadth-first iterate over graph, given as dictionary
"""


class Graph:
    def __init__(self, E):
        self.E = E
        self.nodes = []
        # self.E.keys()

    def __iter__(self):
        self.unvisited = [v for v in E]
        return self

    def __next__(self):
        if not self.unvisited:
            raise StopIteration
        curr = self.unvisited.pop(0)
        if curr not in self.nodes:
                self.nodes.append(curr)
        for t in self.E[curr]:
            if t not in self.nodes:
                self.nodes.append(t)
        return self.nodes


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
