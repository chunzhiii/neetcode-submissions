# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(node):
            if not node:
                return 0
            h_l = dfs(node.left)
            h_r = dfs(node.right)
            h = max(h_l, h_r)
            if abs(h_l - h_r) > 1:
                self.is_balanced = False
            return 1 + h
        dfs(root)
        return self.is_balanced