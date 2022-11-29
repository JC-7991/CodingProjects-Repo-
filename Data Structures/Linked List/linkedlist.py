# Linked lists are an ordered collection of objects. 
# Linked lists differ from lists in the way that they store elements in memory. 
# While lists use a contiguous memory block to store references to their data, 
# linked lists store references as part of their own elements.

class LinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def add(self):
        pass