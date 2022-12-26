class Tree:
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data):
        
        if self.data == data:
            return False

        elif self.data > data:
            
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True

        else:

            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    def find(self, data):
        
        if self.data == data:
            return data
        
        elif self.data > data:
            
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        
        elif self.data < data:
            
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        pass