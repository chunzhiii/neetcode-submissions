class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'Bao&#254'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('Bao&#254')