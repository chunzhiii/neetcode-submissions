from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            signature = ''.join(sorted(s))
            d[signature].append(s)
        return list(d.values())

