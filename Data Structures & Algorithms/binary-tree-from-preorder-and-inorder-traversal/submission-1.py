# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        # Hash map for O(1) inorder lookups
        for idx, val in enumerate(inorder):
            hashmap[val] = idx
        pre_idx = 0 # tracks index of preorder array

        def helper(in_left: int, in_right: int) -> TreeNode:
            nonlocal pre_idx
        
            # Base case: no elements to construct subtree
            if in_left > in_right:
                return None
        
            # Select current root from preorder traversal
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
        
            # Root splits inorder into left and right subtrees
            mid = hashmap[root_val]
        
            # Build left subtree then right subtree
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
        
            return root

        return helper(0, len(inorder) - 1)
