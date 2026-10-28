class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[n-1]] * n
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
            right_idx = n - i - 1
            right[right_idx] = max(height[right_idx], right[right_idx + 1])
        sol = 0
        for i in range(1, n):
            top = min(left[i], right[i])
            if top > height[i]:
                sol += top - height[i]
        return sol
                
                    