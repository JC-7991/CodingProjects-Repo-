from CircularLinkedList import *

class DoublyLinkedList:

    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0

    def add (self, d):
        
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root

        else:
            new_node = Node(d, self.root)