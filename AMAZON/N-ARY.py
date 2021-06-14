class TreeNode:       # class representing individual
    def __init__(self, x):
        self.val = x
        self.children = None

root = TreeNode(1)
node1= TreeNode(100)
node2= TreeNode(200)
node3= TreeNode(300)
children = [node1,node2,node3]
root.children = children
print(root.children)