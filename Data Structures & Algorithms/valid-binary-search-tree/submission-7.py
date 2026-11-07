# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, f, c):
            if not node:
                return True
            if node.left and (node.left.val >= node.val or node.left.val <= f):
                return False
            if node.right and (node.right.val <= node.val or node.right.val >= c):
                return False
            return dfs(node.left, f, min(c, node.val)) and dfs(node.right, max(f, node.val), c)
        return dfs(root, float('-inf'), float('inf'))
    