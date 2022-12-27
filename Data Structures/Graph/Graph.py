class Vertex:

    def __init__(self, n):
        self.name = n
        self.neighbors = set()
    
    def add_neighbor(self, v):
        self.neighbors.add(v)

class Graph:

    vertices = {}

    def add_vertex(self, vertex):
        pass