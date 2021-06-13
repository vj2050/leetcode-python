# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        if root is None:
            return result

        levelsQueue = deque()  # to store only node.val at as per each level
        nodeQueue = deque([root, None])
        orderLtoR = True

        while (len(nodeQueue) > 0):
            # pop value of node from deque as usual, only change is how you store the nodes at each level in alternate order i.e first L to R then R to L and repeat
            currNode = nodeQueue.popleft()

            if currNode:
                # check how to store node in each level list
                if orderLtoR == True:  # Left to Right appending and popping i.e FIFO ; append at tail
                    levelsQueue.append(currNode.val)
                else:  # Right to left; FILO ; append at head i.e left
                    levelsQueue.appendleft(currNode.val)

                # check for their children
                if currNode.left:
                    nodeQueue.append(currNode.left)
                if currNode.right:
                    nodeQueue.append(currNode.right)
            else:
                # we have finished one level ; append to result
                result.append(levelsQueue)
                # separate the levels with help of a delimiter, Empty node, mark this level
                if len(nodeQueue) > 0:  # her eit means it has atleast "None"
                    nodeQueue.append(None)

                levelsQueue = deque()  # fresh queue for the next level
                orderLtoR = not orderLtoR  # reversing order for next level

        return result

obj = Solution()










