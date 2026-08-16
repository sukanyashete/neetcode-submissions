# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root, nodes):
        if root == None:
            nodes.append(-101)
            return
        nodes.append(root.val)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nodesP = []
        nodesQ = []

        if (p == None) and (q == None):
            return True
        elif p == None or q == None:
            return False

        self.preorder(p, nodesP)
        self.preorder(q, nodesQ)

        if nodesP == nodesQ:
            return True
        else:
            return False