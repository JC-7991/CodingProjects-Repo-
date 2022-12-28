# Given the root to a binary search tree, find the second largest node in the tree.

class Node: 
   
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None
           
def secondLargestUtil(root, x):
      
    if root == None or x[0] >= 2: 
        return
  
    secondLargestUtil(root.right, x)

    x[0] += 1

    if x[0] == 2:
        print("2nd largest element is", root.key) 
        return

    secondLargestUtil(root.left, x)
 
def secondLargest(root):
    x = [0] 
    secondLargestUtil(root, x)
  
def insert(node, key):
      
    if node == None:
        return Node(key) 

    if key < node.key: 
        node.left = insert(node.left, key) 

    elif key > node.key: 
        node.right = insert(node.right, key) 

    return node

if __name__ == '__main__':

    root = None
    root = insert(root, 100) 

    insert(root, 90)
    insert(root, 80) 
    insert(root, 70) 
    insert(root, 60) 
    insert(root, 50) 
    insert(root, 40) 
  
    secondLargest(root)