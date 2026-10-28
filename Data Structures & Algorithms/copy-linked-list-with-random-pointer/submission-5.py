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
        pos = {}
        counter = 0
        copy_list = []
        while p:
            copy_list.append(p_copy)
            pos[p] = counter
            nxt_idx = look_up.get(p.next)

            if nxt_idx is not None:
                nxt_copy = copy_list[nxt_idx].random
            elif p.next is not None:
                nxt_copy = Node(x=p.next.val)
            else:
                nxt_copy = None
            pos[p.next] = counter

            rnd = p.random
            rnd_idx = look_up.get(rnd)
            if rnd == p.next:
                p_copy.random = nxt_copy
            elif rnd_idx is not None:
                rnd_copy = copy_list[rnd_idx].random
                p_copy.random = rnd_copy
            elif pos.get(rnd) is not None:
                rnd_copy = copy_list[pos.get(rnd)]
                p_copy.random = rnd_copy
            elif rnd is not None:
                rnd_copy = Node(rnd.val)
                look_up[rnd] = counter
                p_copy.random = rnd_copy
            else:
                p_copy.random = None

            p_copy.next = nxt_copy
            p_copy = p_copy.next
            p = p.next
            counter += 1
        
        return dummy
            
            

            

            




