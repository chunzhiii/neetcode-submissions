class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {i: idx for idx, i in enumerate(nums)}
        for idx, i in enumerate(nums):
            other = target - i
            if other in d and d[other] != idx:
                return sorted((idx, d[other]))
