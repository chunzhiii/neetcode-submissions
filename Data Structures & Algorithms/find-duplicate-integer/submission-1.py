class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[nums[slow]]
            temp = nums[nums[fast]]
            fast = nums[nums[temp]]
            if slow == fast:
                break
        slow_2 = fast
        while True:
            slow = nums[nums[slow]]
            slow_2 = nums[nums[slow_2]]
            if slow == slow_2:
                return nums[nums[slow]]