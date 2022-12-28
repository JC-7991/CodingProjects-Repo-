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
            
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)