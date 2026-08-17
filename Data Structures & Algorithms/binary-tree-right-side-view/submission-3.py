# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #nonlocal level
        ds = [] # result
        level = 0

        def side(root, level):
            #ds.append(root.val)
            nonlocal ds
            if not root:
                return
            #nonlocal level
            if level == len(ds):
                ds.append(root.val)
            
            side(root.right, level+1)
            side(root.left, level+1)

        side(root, level)
        return ds