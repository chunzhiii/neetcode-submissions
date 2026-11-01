from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        look_up = defaultdict(list)
        for i, v in enumerate(nums):
            look_up[v].append(i)
        
        def element_exist(value, l, r):
            indexes = look_up[value]
            for i in indexes:
                if i != l and i != r:
                    return True
            return False

        solution = set()
        while r - l > 1:
            third = 0 - nums[l] - nums[r]
            if third > nums[r]:
                l += 1
                continue
            elif third < nums[l]:
                r -= 1
                continue
            elif element_exist(third, l, r):
                solution.add((nums[l], third, nums[r]))
            if abs(nums[l]) < abs(nums[r]):
                r -= 1
            else:
                l += 1
                
        return [list(l) for l in solution]


            

