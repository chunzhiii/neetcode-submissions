# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def recur(node, depth):
            nonlocal max_diameter
            if not node:
                return depth - 1
            d_l = recur(node.left, depth + 1)
            d_r = recur(node.right, depth + 1)
            diameter = d_l - depth + d_r - depth
            if diameter > max_diameter:
                max_diameter = diameter
            return max(d_l, d_r)
        recur(root, 0)
        return max_diameter

