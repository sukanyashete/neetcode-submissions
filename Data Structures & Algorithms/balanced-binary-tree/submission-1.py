# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Find left height, right height and compare. All the calculations
# done in the calling function only, where height is calculated and the final result whether
# balanced or not balanced is returned. 
# This is done so that no extra time is needed to later compare. 
class Solution:
    def height(self, root):
        if root == None:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)
        if (lh == -1) or (rh == -1):
            return -1
        if (abs(lh-rh) > 1):
            return -1
        
        return max(lh,rh) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = self.height(root) 
        if bal == (-1):
            return False
        else:
            return True
