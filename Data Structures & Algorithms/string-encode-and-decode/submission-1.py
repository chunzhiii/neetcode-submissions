class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'Bao&#254'.join(strs) if strs else '88*6%4'

    def decode(self, s: str) -> List[str]:
        return s.split('Bao&#254') if s != '88*6%4' else []