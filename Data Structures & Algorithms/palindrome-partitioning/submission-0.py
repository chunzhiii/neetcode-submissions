class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(s):
            if not s:
                res.append(cur[:])
                return
            for i in range(len(s)):
                l = s[:i+1]
                if l == l[::-1]:
                    cur.append(l)
                    dfs(s[i+1: ])
                    cur.pop()
        dfs(s)
        return res