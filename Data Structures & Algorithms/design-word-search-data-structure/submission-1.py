class TrieNode:
    def __init__(self):
        self.members = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.node
        for c in word:
            if c not in node.members:
                node.members[c] = TrieNode()
            node = node.members[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.node
        length = len(word)
        self.exist = False
        def dfs(node, index):
            if index >= length:
                if node.end:
                    self.exist = True
                return
            if word[index] != '.':
                if word[index] not in node.members:
                    return
                return dfs(node.members[word[index]], index + 1)
            else:
                for _, child_node in node.members.items():
                    dfs(child_node, index + 1)
        dfs(node, 0)
        return self.exist

