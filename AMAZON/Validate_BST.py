# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=float("-inf"), high=float("inf")):
            # base case
            if not node:
                return True  # empty trees are valid bst

            if node.val <= low or node.val >= high:  # out of bounds
                return False

            # else, all good, now validate its subtrees
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)

obj = Solution()

