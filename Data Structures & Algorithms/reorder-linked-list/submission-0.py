# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        l, r = head, pre
        count = 0
        while l != r:
            if count % 2 == 0:
                nxt = l.next
                l.next = r
                l = nxt
            else:
                nxt = r.next
                r.next = l
                r = nxt
            count += 1
        return

        
            
            

