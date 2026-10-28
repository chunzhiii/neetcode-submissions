class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ''
        for s in strs:
            length = len(s)
            sol += f'{length}#{s}'
        return sol

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sol = []
        pointer = 0
        end = len(s) - 1
        while pointer <= end:
            length_per_str = ''
            word = ''
            while s[pointer] != '#':
                length_per_str += s[pointer]
                pointer += 1
            pointer += 1 # actually point to the str
            for i in range(int(length_per_str)):
                word += s[pointer]
                pointer += 1
            sol.append(word)
        return sol

