# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # node doesnt exist. It is valid. (Base case)
            if not node:
                return True
            # Current node must sit strictly inside (low, high) so that it follows BST property
            if (node.val <= low) or (node.val >= high):
                return False
            # Recursively check left and right subtrees with updated bounds
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))