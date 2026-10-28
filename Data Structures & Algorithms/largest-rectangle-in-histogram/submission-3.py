class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for idx, h in enumerate(heights):
            if not stack or stack[-1][0] <= h:
                stack.append([h, idx])
            else:
                while stack and stack[-1][0] > h:
                    last_height, last_idx = stack.pop()
                    last_area = last_height * (idx - last_idx)
                    max_area = max(last_area, max_area)
                stack.append([h, last_idx])
        while stack:
            last_height, last_idx = stack.pop()
            max_area = max(max_area, last_height * (n - last_idx))
        return max_area