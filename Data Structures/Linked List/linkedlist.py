# Linked lists are an ordered collection of objects. 
# Linked lists differ from lists in the way that they store elements in memory. 
# While lists use a contiguous memory block to store references to their data, 
# linked lists store references as part of their own elements. 

class Node:

    def __init__(self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p