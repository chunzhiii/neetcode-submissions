class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, l):
            if i >= n:
                res.append(l)
                return
            dfs(i + 1, l + [nums[i]])
            dfs(i + 1, l)
        dfs(0, [])
        return res