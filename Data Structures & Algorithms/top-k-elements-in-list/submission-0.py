from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        t = sorted([(frequency, number) for number, frequency in d.items()])[::-1]
        sol = [t[i][1]for i in range(k)]
        return sol
        