class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        candidates.sort()
        def dfs(l, index):
            s = sum(l)
            if s == target:
                res.add(tuple(l))
                return
            if index == n:
                return
            if s > target:
                return
            else:
                nxt_idx = index + 1
                dfs(l + [candidates[index]], nxt_idx)
                while nxt_idx < n and candidates[nxt_idx] == candidates[index]:
                    nxt_idx += 1
                dfs(l, nxt_idx)
        
        dfs([], 0)
        return [list(i) for i in res]