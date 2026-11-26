class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def dfs(l, r, cur):
            if l == 0 and r == 0:
                res.add(cur)
                return
            if l > 0:
                dfs(l - 1, r, cur + '(')
            if r > l:
                dfs(l, r - 1, cur + ')')
        dfs(n, n, '')
        return list(res)