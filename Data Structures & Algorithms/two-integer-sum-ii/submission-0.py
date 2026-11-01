class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        r = n // 2
        l = r - 1
        while l >= 0 and r <= n - 1:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                if r - l == 1:
                    l -= 1
                else:
                    r -= 1
            else:
                if r - l == 1:
                    r += 1
                else:
                    l += 1
        return []