class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return true
            visited.add(num)

        return false