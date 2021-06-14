# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode):
        # ITERATVIE APPROACH : Using Doubly Ended Queue :  O(N) TIME AND SPACE
        levels = []
        if not root:
            return levels
        level = 0
        myQueue = deque([root, ])

        while (myQueue):
            levels.append([])  # new level added
            currLength = len(myQueue)

            for i in range(currLength):
                node = myQueue.popleft()
                levels[level].append(node.val)

                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
            level += 1
        return levels

# RECURSIVE APPROACH : O(N) TIME AND SPACE

#         levels = []
#         if not root:
#             return levels

#         def helper(node, level):
#             if len(levels) == level:
#                 # create a new level
#                 levels.append([])

#             levels[level].append(node.val)

#             # recursively process on its child nodes
#             # also check that node is not none
#             if node.left:
#                 helper(node.left, level+1)
#             if node.right:
#                 helper(node.right, level+1)
#         helper(root, 0)
#         return levels

