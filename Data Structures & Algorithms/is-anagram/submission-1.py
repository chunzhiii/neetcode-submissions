from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for letter in s:
            dict_s[letter] += 1
        for letter in t:
            dict_t[letter] += 1
        
        for k, v in dict_s.items():
            if k not in dict_t or v != dict_t[k]:
                return False
        return True
