# Given pre-order and in-order traversals of a binary tree, 
# write a function to reconstruct the tree.

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def buildTree(inOrder, preOrder, start, end):
     
    if(start > end):
        return None
 
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if start == end:
        return tNode

    inIndex = search(inOrder, start, end, tNode.data)
    tNode.left = buildTree(inOrder, preOrder, start, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, end)
 
    return tNode
 
def search(arr, start, end, value):

    for i in range(start, end + 1):
        if arr[i] == value:
            return i
 
def printOrder(node):

    if node is None:
        return

    printOrder(node.left)
    print(node.data, end = ' ')
    printOrder(node.right)
     
if __name__ == "__main__":

    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

    buildTree.preIndex = 0
    root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

    print("Inorder traversal of the constructed tree:")
    printOrder(root)
 