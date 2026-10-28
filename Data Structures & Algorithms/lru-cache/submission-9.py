class LRUCache:

    def __init__(self, capacity: int):
        self.data = {} #{key: [value, pre, next]}
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        v = self.data.get(key)
        if not v:
            return -1
        if key == self.head:
            return v[0]
        pre = v[1]
        nxt = v[2]
        if pre != None:
            self.data[pre][2] = nxt
        if nxt != None:
            self.data[nxt][1] = pre
        if self.head != key:
            self.data[self.head][1] = key
            self.data[key][2] = self.head
        self.data[key][1] = None
        self.head = key
        if self.tail == key and pre != None:
            self.tail = pre

        return v[0]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            _ = self.get(key)
            self.data[key][0] = value
            return
        
        d = [value, None, self.head]
        self.data[key] = d
        if self.head != None:
            self.data[self.head][1] = key
        self.head = key
        if self.tail == None:
            self.tail = key

        self.size += 1
        if self.size > self.capacity:
            second_to_last = self.data[self.tail][1]
            del self.data[self.tail]
            self.tail = second_to_last
            self.data[second_to_last][2] = None

            



