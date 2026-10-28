class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True
        start, end = 0, n - 1
        while end - start >= 1:
            c1 = s[start].lower()
            c2 = s[end].lower()
            if not c1.isalnum():
                start += 1
                continue
            if not c2.isalnum():
                end -= 1
                continue
            if c1 != c2:
                return False
            start += 1
            end -= 1
        return True
