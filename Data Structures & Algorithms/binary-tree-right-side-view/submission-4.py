# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Method: Recursive so that it is space efficient. Space complexity: O(h) where h is the height of tree.
# Do a reverse pre-order traversal of form: root, right, left
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds = [] # store and return result
        level = 0

        def side(root, level):
            nonlocal ds
            if not root:
                return
                
            # This is so that only the rightmost node gets added into ds and not all nodes in level l.
            # ie. right side recurses first so the rightmost node is added. Now the recursive call goes to 
            # left side. There are chances that there is a node on left on same level (See example 1 nodes 2,3)
            # With this code 3 is visited first by the recursive call and later 2 when 1.left gets called.
            # by the time 1.left is called, len(ds) = 3. Since len(ds) doesnt match the level at 2, that element is not added and that's how we maintain only rightmost element in ds.
            if level == len(ds):
                ds.append(root.val)
            
            side(root.right, level+1)
            side(root.left, level+1)

        side(root, level)
        return ds
