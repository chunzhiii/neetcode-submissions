class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        n = len(prices)
        while l < n and r < n:
            res = max(res, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return res
            