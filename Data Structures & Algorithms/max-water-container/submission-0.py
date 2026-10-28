class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        max_water = -1
        while l < r:
            current = min(heights[l], heights[r]) * (r - l)
            if current > max_water:
                max_water = current
            
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_water
