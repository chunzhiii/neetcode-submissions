class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        sol = [0] * n
        stack = []
        for i in range(n):
            cur = temperatures[i]
            while stack and cur > stack[-1][0]:
                pre_temp, pre_idx = stack.pop()
                sol[pre_idx] = i - pre_idx
            stack.append((cur, i))
        return sol