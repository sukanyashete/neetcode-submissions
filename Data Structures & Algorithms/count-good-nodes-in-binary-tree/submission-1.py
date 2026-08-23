# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        goodnodes = 0
        stack = []
        stack.append(root.val)

        def inorder(root):
            nonlocal goodnodes
            if not root:
                #if stack:
                #    stack.pop()
                return

            if root.val >= stack[-1]:
                goodnodes += 1
                #if stack[-1] != root.val:
            stack.append(max(root.val, stack[-1]))

            inorder(root.left)
            inorder(root.right)
            if stack:
                stack.pop()
                
        inorder(root)
        return goodnodes
