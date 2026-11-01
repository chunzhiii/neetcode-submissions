class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        if total == 1:
            return nums1[0] if nums1 else nums2[0]
        half = total // 2
        is_odd = total % 2 != 0
        c2 = 0
        l, r = 0, n - 1
        while l <= r:
            print(l, r)
            mid = l + (r - l) // 2
            b_num2 = mid + 1
            b_num1 = half - b_num2
            if nums1 and b_num1 >= 0 and nums1[b_num1] < nums2[mid]:
                r = mid - 1
            else:
                l = mid + 1
                c2 = mid
        if 0 < c2 < n:
            max_2 = nums2[c2-1]
            max_left = max_2
            if nums1:
                max_left = max(max_left, nums1[half-c2-1])
            min_right = nums2[c2]
            if nums1:
                min_right = min(min_right, nums1[half-c2])
        elif c2 == 0:
            max_left = nums1[half - 1]
            if nums2:
                min_right = nums2[0]
            elif nums1:
                min_right = nums1[half]
            if m > half:
                min_right = min(min_right, nums1[half])
        else:
            max_left = nums2[n-1]
            if half > n:
                max_left = max(max_left, nums1[half-n-1])
            min_right = max_left
            if nums1:
                min_right = nums1[half-n]
        if is_odd:
            return min_right
        else:
            return (min_right + max_left)/2
        




