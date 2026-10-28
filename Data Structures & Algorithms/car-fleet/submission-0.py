class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        look_up = list(zip(position, speed))
        look_up.sort(reverse=True)
        stack = []
        for pos, v in look_up:
            t = (target - pos)/v
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)