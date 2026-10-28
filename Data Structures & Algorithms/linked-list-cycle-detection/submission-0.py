# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        pt = head
        while pt:
            if pt not in visited:
                visited.add(pt)
                pt = pt.next
            else:
                return True
        return False