# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        d.append(root)
        res = []
        while d:
            l = []
            for i in range(len(d)):
                node = d.popleft()
                if node:
                    l.append(node.val)
                    d.append(node.left)
                    d.append(node.right)
            if l:
                res.append(l)
        return res