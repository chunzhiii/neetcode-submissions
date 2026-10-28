class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = set(nums)
        look_up = dict()
        stack = []
        for i in nums:
            if i in look_up:
                continue
            stack.append(i)
            while stack:
                current = stack[-1]
                nxt = current + 1
                if nxt in look_up:
                    look_up[current] = 1 + look_up[nxt]
                    stack.pop()
                elif nxt not in unique:
                    look_up[current] = 1
                    stack.pop()
                else:
                    stack.append(nxt)
        return max(look_up.values())
        
            
            
                

