class Vertex:

    def __init__(self, n):
        self.name = n
        self.neighbors = set()
    
    def add_neighbor(self, v):
        self.neighbors.add(v)

class Graph:

    vertices = {}

    def add_vertex(self, vertex):
        
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        pass