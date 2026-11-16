class PrefixTree:

    def __init__(self):
        self.members = {}
        self.end = False

    def insert(self, word: str) -> None:
        for c in word:
            if c not in self.members:
                new = PrefixTree()
                self.members[c] = new
            self = self.members[c]
        self.end = True

    def search(self, word: str) -> bool:
        for c in word:
            if c not in self.members:
                return False
            self = self.members[c]
        return self.end

    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            if c not in self.members:
                return False
            self = self.members[c]
        return True
        