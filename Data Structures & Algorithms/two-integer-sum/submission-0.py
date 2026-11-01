class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {i: idx for idx, i in enumerate(nums)}
        for value, index in d.items():
            other = target - value
            if other in d:
                return sorted((index, d[other]))
                