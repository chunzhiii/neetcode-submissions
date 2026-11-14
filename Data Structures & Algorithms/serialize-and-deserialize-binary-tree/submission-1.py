# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '[]'
        q = deque([root])
        res = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append(None)
        return str(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = eval(data)
        if not q:
            return None
        res = root = TreeNode(q[0])
        stack = deque([root])
        n = len(q)
        c = 1
        while c < n:
            node = stack.popleft()
            l = q[c]
            if l is not None:
                left_node = TreeNode(l)
                node.left = left_node
                stack.append(left_node)
            c += 1
            r = q[c]
            if r is not None:
                right_node = TreeNode(r)
                node.right = right_node
                stack.append(right_node)
            c += 1
        return res

        




