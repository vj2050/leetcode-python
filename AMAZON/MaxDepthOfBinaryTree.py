'''  Binary tree to build :
          1
        /  \
       9    4
     /    /  \
    8    7    6

Print out simple BFS traversal
'''
class TreeNode:       # class representing individual
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
result = []

def printNodes(root):
    queue = [root]

    while(queue):
        node = queue.pop(0)
        if node is not None:
            result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(4)
root.left.left = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(6)
print(printNodes(root))





