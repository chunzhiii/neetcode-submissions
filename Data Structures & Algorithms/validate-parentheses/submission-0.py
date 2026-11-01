class Solution:
    def isValid(self, s: str) -> bool:
        look_up = {
            '(':')',
            '{': '}',
            '[': ']'
        }
        if len(s) == 1:
            return False
        stack = [s[0]]
        for c in s[1:]:
            if c in look_up:
                stack.append(c)
            else:
                last = stack.pop()
                if c != look_up[last]:
                    return False
        return True