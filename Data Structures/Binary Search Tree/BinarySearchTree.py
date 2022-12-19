class Tree:
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data):
        
        if self.data == data:
            return False