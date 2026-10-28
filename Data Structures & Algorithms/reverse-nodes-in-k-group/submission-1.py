# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre_group = dummy

        def get_kth_node(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            kth_node = get_kth_node(pre_group, k)
            if not kth_node:
                break
            next_group = kth_node.next
            pre = kth_node.next
            curr = pre_group.next
            while curr != next_group:
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            tmp = pre_group.next
            pre_group.next = kth_node
            pre_group = tmp
        
        return dummy.next

            

                