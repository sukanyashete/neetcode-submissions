# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #using the referance of max depth problem to solve this one
        max_diameter = 0

        def depth(node):
            nonlocal max_diameter
            if node == None:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            max_diameter = max(max_diameter, left+right)

            return 1 + max(left, right)

        depth(root)
        return max_diameter