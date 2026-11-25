class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        def dfs(l, index):
            res.add(tuple(l))
            if index == n:
                return
            nxt_idx = index + 1
            dfs(l + [nums[index]], nxt_idx)
            while nxt_idx < n and nums[nxt_idx] == nums[index]:
                nxt_idx += 1
            dfs(l, nxt_idx)
        dfs([], 0)
        res = [list(i) for i in res]
        return res
            