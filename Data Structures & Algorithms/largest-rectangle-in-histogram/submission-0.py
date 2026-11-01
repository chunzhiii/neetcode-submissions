class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for h in heights:
            for i in range(len(stack)):
                previous_height, width = stack[i]
                new_height = min(previous_height, h)
                new_width = width + 1
                if new_height * new_width > max_area:
                    max_area = new_height * new_width
                stack[i][0] = new_height
                stack[i][1] = new_width
            if h > max_area:
                max_area = h
            stack.append([h, 1])
        return max_area
                