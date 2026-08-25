# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder traversal in BST gives elements in sorted order.
# Maintaining a cnt variable which keeps incrementing by 1. Matching it with requested k.
# returning the resultant variable when cnt == k 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def inorder(root):
            nonlocal cnt
            if not root:
                return

            leftval = inorder(root.left)
            if leftval:
                return leftval
            cnt += 1
            if cnt == k:
                return root.val
            
            return inorder(root.right)
        
        return(inorder(root))
        