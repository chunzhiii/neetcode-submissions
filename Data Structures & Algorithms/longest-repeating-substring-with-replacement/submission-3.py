class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        look_up = {}
        n = len(s)
        res = 0
        for r in range(n):
            look_up[s[r]] = 1 + look_up.get(s[r], 0)
            while r - l + 1 - max(look_up.values()) > k:
                look_up[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
        
