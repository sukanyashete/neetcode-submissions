# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Explanation: Operation done with a global variable instead of a non-local variable.
# The max diameter possible at a node is its left height + right height. 
# Use the same loop as in finding max depth of binary tree. In that we already find out left and right height.
# using that height value to manipulate and find out diameter.
# diameter keeps updating itself everytime based on the new left and right heights calculated
# method height() returns the max height of the tree from that specific node.
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
        self.height(root)
        return self.diameter