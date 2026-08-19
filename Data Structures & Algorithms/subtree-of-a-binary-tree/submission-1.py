# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if tree exists and no subtree, empty subtree is a valid subtree of tree so return True
        if not subRoot:
            return True
        # if the main tree doesnt exist then there is no point of checking its subtree
        # we cant say it is a subtree of the main tree
        if (not root) and subRoot:
            return False

        # helper function to check the similarity between two trees
        def isSameTree(root, subroot):
            # while recursive visits both nodes get null
            if (not root) and (not subroot):
                return True
            # not valid if either of root or subroot becomes null or their values doesnt match.
            if (not root) or (not subroot) or (subroot.val != root.val):
                return False
            # keep comparing its left and right trees with subtrees to confirm on the match
            return isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right)

        # just checks the parent node of both trees, only one iteration
        if isSameTree(root, subRoot):
            return True

        # since the parent node was different now moving to the next iteration levels.
        # going to its child node. 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
