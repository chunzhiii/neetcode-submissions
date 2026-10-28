class Solution:
    def isValid(self, s: str) -> bool:
        look_up = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if len(s) == 1:
            return False
        stack = []
        if s[0] in look_up:
            stack.append(s[0])
        else:
            return False

        for c in s[1:]:
            if c in look_up:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c != look_up[last]:
                    return False
        if stack:
            return False
        return True