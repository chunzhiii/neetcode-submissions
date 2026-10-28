class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        total = len(a) + len(b)
        half = total // 2

        while True:
            i = l + (r - l) // 2
            j = half - i - 2
            a_left = a[i] if i >= 0 else float('-inf')
            a_right = a[i+1] if (i + 1) < len(a) else float('inf')
            b_left = b[j] if j >= 0 else float('-inf')
            b_right = b[j+1] if (j + 1) < len(b) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2 != 0:
                    return min(a_right, b_right)
                else:
                    return (min(a_right, b_right) + max(a_left, b_left)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1