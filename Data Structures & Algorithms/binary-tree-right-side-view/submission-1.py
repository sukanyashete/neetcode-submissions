# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        result = []
        reading = deque([root])

        while reading:
            buffer = []
            length = len(reading)
            for i in range(length):
                x = reading.popleft()
                buffer.append(x)
                if x.left:
                    reading.append(x.left)
                if x.right:
                    reading.append(x.right)
            result.append(buffer[-1].val)

        return result