class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l ) // 2
            mid_val = nums[mid]
            if r - l == 1:
                return min(nums[l], nums[r])
            elif mid_val < nums[(mid - 1) % n]:
                return mid_val
            elif nums[l] < nums[r]:
                return nums[l]
            elif nums[l] < mid_val:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1