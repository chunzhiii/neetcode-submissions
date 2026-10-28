# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        sol = None
        cur = None

        while p1 and p2:
            if p1.val <= p2.val:
                nxt = p1
                p1 = p1.next
            else:
                nxt = p2
                p2 = p2.next
            if not cur:
                cur = nxt
                sol = nxt
            else:
                cur.next = nxt
                cur = cur.next
        
        while p1:
            if not cur:
                cur = p1
                sol = cur
            else:   
                cur.next = p1
                cur = cur.next
            p1 = p1.next
        while p2:
            if not cur:
                cur = p2
                sol = cur
            else:    
                cur.next = p2
                cur = cur.next
            p2 = p2.next

        return sol
