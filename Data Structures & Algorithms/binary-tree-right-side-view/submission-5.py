# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Logic: Do Level order traversal (BFS), in each level the last node is the one from right view.
# iterative method
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        result = [] # solution array
        reading = deque([root]) # live array to keep elements read

        while reading:
            buffer = [] # to hold elements in the same level, used to find the rightmost element later
            length = len(reading)
            for i in range(length):
                x = reading.popleft()
                buffer.append(x)
                if x.left:
                    reading.append(x.left)
                if x.right:
                    reading.append(x.right)
            # Appending the rightmost element to result
            result.append(buffer[-1].val)

        return result
