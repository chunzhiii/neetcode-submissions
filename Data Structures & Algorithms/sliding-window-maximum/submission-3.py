from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        sol = []
        for i in range(k):
            while d and nums[i] > d[-1][0]:
                d.pop()
            d.append((nums[i], i))
        sol.append(d[0][0])
        for i in range(k, len(nums)):
            if d[0][1] <= i - k:
                d.popleft()
            while d and nums[i] > d[-1][0]:
                d.pop()
            d.append((nums[i], i))
            sol.append(d[0][0])
        return sol