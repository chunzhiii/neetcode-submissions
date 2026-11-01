# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val != q.val:
                return False
            is_same_l = self.isSameTree(p.left, q.left)
            is_same_r = self.isSameTree(p.right, q.right)
            return is_same_l and is_same_r