from Vertex import *

class Graph:

    vertices = {}

    def add_vertex(self, vertex):
        
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True

        else:
            return False

    def add_edge(self, u, v):
        
        if u in self.vertices and v in self.vertices:
            
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        
        else:
            return False