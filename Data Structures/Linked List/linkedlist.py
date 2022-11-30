# Linked lists are an ordered collection of objects. 
# Linked lists differ from lists in the way that they store elements in memory. 
# While lists use a contiguous memory block to store references to their data, 
# linked lists store references as part of their own elements.

from NodeClass import Node

class LinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    
    def find(self, d):

        this_node = self.root

        while this_node is not None:

            if this_node.data == d:
                return d

            else:
                this_node = this_node.next_node
        
        return None

    def remove(self, d):
        
        this_node = self.root
        prev_node = None

        while this_node is not None:
            
            if this_node.data == d:

                if prev_node is not None:
                    prev_node.next_node == this_node.next_node

                else:
                    self.root = this_node.next_node

                self.size -= 1

                return True

            else:
                prev_node = this_node
                this_node = this_node.next_node

        return False

    def print_list(self):
        
        this_node = self.root

        while this_node is not None:
            print(this_node, end = '->')
            this_node = this_node.next_node
            
        print('None')