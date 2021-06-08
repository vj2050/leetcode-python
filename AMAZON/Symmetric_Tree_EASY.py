# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        def isMirrorHelper(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False

            if left.val == right.val:  # roots are same, proceed to check child nodes symmetry
                return isMirrorHelper(left.left, right.right) and isMirrorHelper(left.right, right.left)

        # else, check for symmetry in left and right subtree
        return isMirrorHelper(root.left, root.right)

