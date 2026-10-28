class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        n = len(s)
        unique = set()
        while r < n:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            r += 1
            res = max(res, r - l)
        return res

