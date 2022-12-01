from LinkedList import *

class CircularLinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):

        if self.size == 0:
            self.root = Node(d)
            self.root.next_node == self.root
        
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node