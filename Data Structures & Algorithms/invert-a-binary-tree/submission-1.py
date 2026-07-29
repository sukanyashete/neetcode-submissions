# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        # Swapping left and right children
        root.left, root.right = root.right, root.left

        # Recursing on the left child
        self.invertTree(root.left)
        # Recursing on the right child
        self.invertTree(root.right)

        # Return its root as requested
        return root