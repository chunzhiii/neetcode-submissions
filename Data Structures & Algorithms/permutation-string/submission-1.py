from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        
        for l in range(n2 - n1 + 1):
            r = l + n1
            current_s = s2[l:r]
            d_cur = defaultdict(int)
            for c in current_s:
                d_cur[c] += 1
            if d1 == d_cur:
                return True
        
        return False

