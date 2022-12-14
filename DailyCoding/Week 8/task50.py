# Suppose an arithmetic expression is given as a binary tree. 
# Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
# Given the root to such a tree, write a function to evaluate it.

class node:

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
 
def evalTree(root):
 
    if root is None:
        return 0
 
    if root.left is None and root.right is None:
        return int(root.data)
 
    left_sum = evalTree(root.left)
    right_sum = evalTree(root.right)
 
    if root.data == '+':
        return left_sum + right_sum
 
    elif root.data == '-':
        return left_sum - right_sum
 
    elif root.data == '*':
        return left_sum * right_sum
 
    else:
        return left_sum // right_sum
 
if __name__ == "__main__":
 
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('-4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')
    print(evalTree(root))
 
    root = None
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print(evalTree(root))