class CircularLinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            pass