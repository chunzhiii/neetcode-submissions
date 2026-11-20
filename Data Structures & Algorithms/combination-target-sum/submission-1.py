class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(index, l):
            if index >= n:
                return
            s = sum(l)
            if s == target:
                res.append(l)
                return
            elif s > target:
                return
            else:
                dfs(index, l + [nums[index]])
                dfs(index + 1, l)
        dfs(0, [])
        return res