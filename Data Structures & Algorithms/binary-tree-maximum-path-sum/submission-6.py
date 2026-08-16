# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Explanation: Followed striver's video.
# Used the logic from problems max depth of binary tree, diameter of binary tree
# The same recursive looping to traverse nodes as in max depth of binary tree.
# The way to calculate depth when recursive loop happens same as in diameter of binary tree
# The sum is found with node.vals since we are calculating max path sum. 
# leftsum<0 and rightsum<0 done so that we shouldnt consider any path which has -ve sum because it lowers the total cost of path. we have to maximimze so donot consider the side if its sum is negative.
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

            maxsum = max(maxsum, root.val + leftsum + rightsum)

            return root.val + max(leftsum, rightsum)

        pathsum(root)
        return maxsum
        