# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq, itertools
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        cnt = itertools.count()
        for l in lists:
            while l:
                heapq.heappush(h, (l.val, next(cnt), l))
                l = l.next
            
        dummy = p = ListNode()
        while h:
            _, _, min_node = heapq.heappop(h)
            p.next = min_node
            p = p.next
        return dummy.next

                
