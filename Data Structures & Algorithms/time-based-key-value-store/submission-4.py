from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.look_up = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.look_up[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = self.look_up.get(key, '')
        if not val:
            return ""
        l, r = 0, len(val) - 1
        sol = ""
        while l <= r:
            mid = l + (r - l) // 2
            if val[mid][0] <= timestamp:
                sol = val[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return sol
