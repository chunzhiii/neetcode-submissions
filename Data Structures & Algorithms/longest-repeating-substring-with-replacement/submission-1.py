class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        look_up = [0] * 26
        n = len(s)
        res = 0
        def is_valid(length):
            max_count = 0
            for i in range(26):
                max_count = max(max_count, look_up[i])
            return length - max_count <= k
            
        for r in range(n):
            new_c_index = ord(s[r]) - ord('A')
            look_up[new_c_index] += 1
            while not is_valid(r - l + 1):
                left_c_index = ord(s[l]) - ord('A')
                look_up[left_c_index] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res


        
