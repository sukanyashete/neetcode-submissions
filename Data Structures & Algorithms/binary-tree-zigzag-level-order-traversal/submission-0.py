# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result

        ltor = True # Flag to indicate the reading direction left-to-right/right-to-left
        readingQ = deque([root])
        row = []

        while readingQ:
            
            length = len(readingQ)
            for i in range(length):
                node = readingQ.popleft()
                row.append(node.val)
                if node.left:
                    readingQ.append(node.left)
                if node.right:
                    readingQ.append(node.right)
            if ltor:
                #if row:
                #print("row is ", row)
                result.append(row)
                ltor = False
            elif not ltor: #ltor is false
                #print("row before reverse ", row)
                row.reverse()
                #print("row after reverse ", row)
                result.append(row)
                ltor = True
            row = []

        return result