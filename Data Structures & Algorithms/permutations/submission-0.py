class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        n = len(nums)
        res = []
        def dfs(l):
            if len(l) == n:
                res.append(l)
                return
            
            for i in range(n):
                if i in visited:
                    continue
                visited.add(i)
                dfs(l + [nums[i]])
                visited.remove(i)
        dfs([])
        return res