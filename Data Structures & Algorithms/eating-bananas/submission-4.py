import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            h_min = sum((math.ceil(i / mid) for i in piles))
            h_min_plus = sum((math.ceil(i / (mid - 1)) for i in piles)) if mid > 1 else float('inf')
            if h_min <= h and h_min_plus > h:
                return mid
            elif h_min > h:
                l = mid + 1
            else:
                r = mid - 1
        return -1