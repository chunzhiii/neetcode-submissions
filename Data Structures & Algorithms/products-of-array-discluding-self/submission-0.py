class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, sol = [1] * n, [1] * n, [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right_pointer = n - i - 1
            right[right_pointer] = right[right_pointer + 1] * nums[right_pointer + 1]
        
        for i in range(n):
            sol[i] = left[i] * right[i]
        return sol
