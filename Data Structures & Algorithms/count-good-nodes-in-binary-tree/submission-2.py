# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Tree is empty so no good nodes. return 0
        if not root:
            return 0

        goodnodes = 0
        # Explicit stack to track the maximum value seen along the current path from root to node.
        # init with root.val so as to use as first value to start comparing
        stack = []
        stack.append(root.val)

        # Preorder Traversal (Root -> Left -> Right)
        # We use preorder because a child node needs to know the max value from its parent 
        # before it can decide whether it is a "good node".
        def preorder(root): 
            nonlocal goodnodes
            if not root:
                return
            # stack[-1] holds the maximum value seen from the root down to the current node's parent.
            if root.val >= stack[-1]:
                goodnodes += 1
            # Push the updated max value onto the stack for the upcoming child calls.
            # ensures both left and right subtrees inherit the new path maximum. //Step 2 here
            stack.append(max(root.val, stack[-1]))

            preorder(root.left)
            preorder(root.right)

            # Pop the max value pushed in Step 2 so that when execution returns back to 
            # the parent node, the stack top correctly reflects the parent's path state again.
            if stack:
                stack.pop()

        preorder(root)
        return goodnodes
