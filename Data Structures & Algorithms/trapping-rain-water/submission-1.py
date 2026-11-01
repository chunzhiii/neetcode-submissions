class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, height.index(max(height))
        n = len(height)
        sol = 0
        for i in range(n):
            if height[i] >= height[l]:
                l = i
            if i <= r:
                top = min(height[l], height[r])
                added_amount = top - height[i]
                sol += added_amount
            else:
                l = r
                if i + 1 <= n - 1:
                    new = height[i+1:]
                    r = new.index(max(new)) + i + 1

                top = min(height[l], height[r])
                delta = (top - height[i]) 
                added_amount = delta if delta > 0 else 0
                sol += added_amount
        return sol
                
                    