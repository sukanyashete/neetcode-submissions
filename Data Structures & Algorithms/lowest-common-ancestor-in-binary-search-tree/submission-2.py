# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # root is null, either p or q = root means that is the lowest common. 
        # if it goes below then the splitup starts which will eventually have the current p or q as 
        # the lowest common.
        if (not root) or (p == root) or (q == root):
            return root

        # traversing to find left and right subtree
        # if element found, return the element
        # if element not found, return None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # When both the nodes P and Q are child of current root node, we found the LCA.
        if left and right:
            return root
        # Parent's right node returned NULL. which means one of the nodes that we are searching for is on that path. Left returned a positive value which means we found one of the nodes that we are searching for on left
        elif left:
            return left
        # Parent's left node returned NULL. which means one of the nodes that we are searching for is on that path. right returned a positive value which means we found one of the nodes that we are searching for on right
        elif right:
            return right


# Going down a tree from root. Left/Right child can return the value of node to parent if that is the node we are looking for. Parent checks if any of its side(left/right) returned any value. If it got None from both sides it returns Null to its parent and if the value reaching the parent is <int> and Null, it returns the Null. This confirms that atleast one value of that we are looking for is found. The LCA is confirmed when both the left and right sides of the parent return a <int> value. Due to the recursive call, the lowest common ancestor would be the one which will hit both its left and right child <int>, none of them is None. We return immediately. 