from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        temp = defaultdict(int)
        score = 0
        for c in t:
            d[c] += 1
        target_score = len(d)
        l, r = 0, 0
        min_left, min_right = 0, -1
        min_length = float('inf')
        while True:
            #print(temp, score, min_length)
            if score == target_score:
                #print("im here")
                if (r - l + 1 ) < min_length:
                    min_length = r - l + 1
                    min_left = l
                    min_right = r
                temp[s[l]] -= 1
                if temp[s[l]] < d[s[l]]:
                    score -= 1
                l += 1
                continue
            if r == len(s):
                break
            temp[s[r]] += 1
            if temp[s[r]] == d[s[r]]:
                score += 1
            # if score == len(t) and (r - l + 1) < min_length:
            #     min_length = r - l + 1
            #     min_left = l
            #     min_right = r
            r += 1
        
        return s[min_left: min_right] if min_right >=0 else ''
