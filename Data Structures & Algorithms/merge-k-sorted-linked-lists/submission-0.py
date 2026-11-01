# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = p = ListNode()
        while any(lists):
            min_idx = -1
            min_val = float('inf')
            for idx, node in enumerate(lists):
                if node and node.val < min_val:
                    min_node = node
                    min_idx = idx
                    min_val = node.val
            p.next = min_node
            p = p.next
            lists[min_idx] = min_node.next
        return dummy.next

                
