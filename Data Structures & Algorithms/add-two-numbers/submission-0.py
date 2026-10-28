# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol = p = ListNode()
        carry_over = 0
        while l1 and l2:
            val = l1.val + l2.val + carry_over
            digit = val % 10
            carry_over = val // 10
            p.val = digit
            if l1.next or l2.next or carry_over:
                p.next = ListNode()
                p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry_over
            digit = val % 10
            carry_over = val // 10
            p.val = digit
            if l1.next or carry_over:
                p.next = ListNode()
                p = p.next
            l1 = l1.next
        while l2:
            val = l2.val + carry_over
            digit = val % 10
            carry_over = val // 10
            p.val = digit
            if l2.next or carry_over:
                p.next = ListNode()
                p = p.next
            l2 = l2.next
        if carry_over:
            p.val = carry_over
        return sol
