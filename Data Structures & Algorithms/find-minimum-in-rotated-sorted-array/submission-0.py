class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            print(l, r)
            mid = l + (r - l ) // 2
            mid_val = nums[mid]
            if mid_val < nums[(mid - 1) % n]:
                return mid_val
            elif nums[l] < mid_val:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1