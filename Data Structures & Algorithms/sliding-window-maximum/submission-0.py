from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        sol = []
        for i in range(k):
            while d and nums[i] > d[-1]:
                d.pop()
            d.append(nums[i])
        sol.append(d[0])
        for i in range(k, len(nums)):
            while d and nums[i] > d[-1]:
                d.pop()
            d.append(nums[i])
            if len(d) > k:
                d.popleft()
            sol.append(d[0])
        return sol