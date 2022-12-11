from CircularLinkedList import *

class DoublyLinkedList:

    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0

    def add(self, d):
        
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root

        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        
        self.size += 1

    def find(self, d):
        
        this_node = self.root

        while this_node is not None:
            
            if this_node.data == d:
                pass