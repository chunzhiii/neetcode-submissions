class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1_set = set(s1)
        for l in range(n2 - n1 + 1):
            r = l + n1
            current_s = s2[l:r]
            if set(current_s) == set(s1_set):
                return True
        
        return False

