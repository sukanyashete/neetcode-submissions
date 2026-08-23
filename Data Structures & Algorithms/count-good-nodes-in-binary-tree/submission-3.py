# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # 1 if current node is "good", else 0
            is_good = 1 if node.val >= max_val else 0
            
            # Update the max path value for child recursive calls
            new_max = max(max_val, node.val)
            
            # Accumulate counts from left and right subtrees
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)