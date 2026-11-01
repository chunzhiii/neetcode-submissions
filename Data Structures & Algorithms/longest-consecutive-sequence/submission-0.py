from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        look_up = defaultdict(int)
        
        def consecutive_iterative(i):
            if i in look_up:
                return look_up[i]
            nxt = i + 1
            if nxt not in unique:
                look_up[i] = 1
                return 1
            count = 1 + consecutive_iterative(i + 1)
            return count

        return max(consecutive_iterative(i) for i in nums)
        
            
            
                

