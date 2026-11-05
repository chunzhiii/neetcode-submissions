# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.look_up = []
        def dfs(node, layer):
            if not node:
                return
            if not self.look_up or layer > self.look_up[-1][0]:
                self.look_up.append((layer, node.val))
            dfs(node.right, layer + 1)
            dfs(node.left, layer + 1)
        dfs(root, 0)
        res = [i[1] for i in self.look_up]
        return res