# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        p = head
        while p:
            counter += 1
            p = p.next
        if counter == 1:
            return None
        p = head
        n_move = counter - n - 1
        if n_move < 0:
            return head.next
        for i in range(n_move):
            p = p.next
        target = p.next
        p.next = target.next
        return head
