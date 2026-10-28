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
        stack = []
        stack.append((l, r))
        visited = set()
        while stack:
            l, r = stack.pop()
            if (l, r) in visited:
                continue
            else:
                visited.add((l, r))
            if r - l < 2:
                continue
            third = 0 - nums[l] - nums[r]
            if third > nums[r]:
                stack.append((l + 1, r))
                continue
            elif third < nums[l]:
                stack.append((l, r - 1))
                continue
            elif element_exist(third, l, r):
                solution.add((nums[l], third, nums[r]))
            stack.append((l + 1, r))
            stack.append((l, r - 1))

                
        return [list(l) for l in solution]


            

