# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1: An empty subRoot is always a valid subtree of any tree
        if not subRoot:
            return True
        
        # Base case 2: A non-empty subRoot cannot be a subtree of an empty main tree
        if not root:
            return False

        # Helper function: Check if two trees are structurally identical with equal values
        def isSameTree(root1, root2):
            # Both nodes are empty -> identical at this path
            if not root1 and not root2:
                return True
            
            # One node is empty or values differ -> not identical
            if not root1 or not root2 or root1.val != root2.val:
                return False
            
            # Recursively check left and right subtrees
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        # Step 1: Check if the current tree starting at 'root' matches 'subRoot'
        if isSameTree(root, subRoot):
            return True

        # Step 2: If not identical at the current root, recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)