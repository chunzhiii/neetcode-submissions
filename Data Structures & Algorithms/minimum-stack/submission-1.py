class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_val = val
    def pop(self) -> None:
        self.stack.pop()
        self.min_val = min(self.stack)

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.min_val
