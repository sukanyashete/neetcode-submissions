# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        
        def pathsum(root):
            nonlocal maxsum
            if root == None:
                return 0

            leftsum = pathsum(root.left)
            if leftsum < 0:
                leftsum = 0
            rightsum = pathsum(root.right)
            if rightsum < 0:
                rightsum = 0

            #maxsum = max(maxsum, root.val)
            #maxsum = max(maxsum, leftsum + root.val)
            #maxsum = max(maxsum, rightsum + root.val)
            maxsum = max(maxsum, root.val + leftsum + rightsum)

            return root.val + max(leftsum, rightsum)

        pathsum(root)
        return maxsum
        