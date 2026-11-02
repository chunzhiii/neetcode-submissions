# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(node, sub_node):
            if not node and not sub_node:
                return True
            elif not node or not sub_node or node.val != sub_node.val:
                return False
            left_same = is_same(node.left, sub_node.left)
            right_same = is_same(node.right, sub_node.right)
            return left_same and right_same
        
        def dfs(node, sub_root):
            if not node:
                return False
            if is_same(node, sub_root):
                return True
            return dfs(node.left, sub_root) or dfs(node.right, sub_root)
        
        return dfs(root, subRoot)
            