class Vertex:

    def __init__(self, n):
        self.name = n

class Graph:

    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):

        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:

            self.vertices[vertex.name] = vertex
            
            for row in self.edges:
                row.append(0)