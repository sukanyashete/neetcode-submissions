# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    diameter = 0
    def height(self, root):
        if root == None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #nonlocal diameter
        #diameter = float('inf')
        self.height(root)

        return self.diameter