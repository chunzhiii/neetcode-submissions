# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            node_value = max(node.val, node.val + left_sum, node.val + right_sum)
            sum_path = node.val
            if left_sum > 0:
                sum_path += left_sum
            if right_sum > 0:
                sum_path += right_sum
            self.max_path_sum = max(self.max_path_sum, sum_path)
            
            return node_value
        
        dfs(root)
        return self.max_path_sum