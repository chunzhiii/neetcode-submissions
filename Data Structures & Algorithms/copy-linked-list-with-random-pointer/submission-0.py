"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p = head
        p_copy = dummy = Node(x=p.val)
        look_up = {}
        counter = 0
        copy_list = []
        while p:
            copy_list.append(p_copy)
            look_up[p]= counter
            nxt = p.next
            copy_nxt = Node(nxt.val) if nxt else None
            p_copy.next = copy_nxt
            p = p.next
            p_copy = p_copy.next
            counter += 1
        p = head
        p_copy = dummy
        while p:
            random_idx = look_up.get(p.random, None)
            p_copy.random = copy_list[random_idx] if random_idx is not None else None
            p = p.next
            p_copy = p_copy.next
        return dummy



