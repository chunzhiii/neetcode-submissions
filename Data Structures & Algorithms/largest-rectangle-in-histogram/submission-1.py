class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for h in heights:
            new_stack = []
            pre_min = 0
            for i in range(len(stack)):
                previous_height, width = stack[i]
                new_height = min(previous_height, h)
                new_width = width + 1
                if new_height <= pre_min:
                    continue
                pre_min = new_height
                new_stack.append([new_height, new_width])
                area = new_height * new_width
                if area > max_area:
                    max_area = area

            if h > pre_min:
                new_stack.append([h, 1])
            if h > max_area:
                max_area = h
            stack = new_stack
        return max_area
                