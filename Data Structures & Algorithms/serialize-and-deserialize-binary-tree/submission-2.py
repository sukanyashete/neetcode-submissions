# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    # Using the logic of BFS (Level order insertion) to traverse the tree and insert in queue
    # empty nodes are marked as 'X'
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        ans = []

        while queue:
            x = queue.popleft()
            if x:
                ans.append(str(x.val))
                queue.append(x.left)
                queue.append(x.right)
            else:
                ans.append("X")

        return ",".join(ans)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if (not data) or (data[0] == 'X'):
            return
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        que = deque([root])
        i = 1

        while (que) and (i < len(nodes)):
            parent = que.popleft()

            if nodes[i] != 'X':
                parent.left = TreeNode(int(nodes[i]))
                que.append(parent.left)
            else:
                parent.left = None
            i += 1
            
            if nodes[i] != 'X':
                parent.right = TreeNode(int(nodes[i]))
                que.append(parent.right)
            else:
                parent.right = None
            i += 1

        return root
