class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:
        p = self.head
        while True:
            k, v = p.val
            if k == key:
                self.head = p
                self.tail = self.head.pre
                return v
            if p != self.tail:
                p = p.next
            else:
                break
        return -1

    def put(self, key: int, value: int) -> None:
        node = (key, value)
        print(node)
        old_head = self.head
        self.head = Node(node)
        self.head.next = old_head
        if old_head:
            old_head.pre = self.head
            self.tail.next = self.head
            self.head.pre = self.tail
        else:
            self.head.next = self.head
            self.tail = self.head
            self.head.pre = self.head        
        if self.size < self.capacity:
            self.size += 1
        else:
            second_to_last = self.tail.pre
            second_to_last.next = self.head
            self.head.pre = second_to_last
            self.tail = second_to_last


        
