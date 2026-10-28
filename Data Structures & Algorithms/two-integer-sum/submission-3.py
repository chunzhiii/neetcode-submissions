class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            other = target - i
            if other in d:
                return [d[other], idx]
            d[i] = idx
