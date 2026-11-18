class Trie:
    def __init__(self):
        self.members = {}
        self.word = ''
    
    def add_word(self, word):
        for c in word:
            if c not in self.members:
                self.members[c] = Trie()
            self = self.members[c]
        self.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.add_word(word)
        rows = len(board)
        cols = len(board[0])
        res = set()
        def dfs(i, j, node):
            if (i < 0 or i >= rows) or (j < 0 or j >= cols) or ((i, j) in visited) or (board[i][j] not in node.members):
                return
            visited.add((i, j))
            new_node = node.members[board[i][j]]
            if new_node.word:
                res.add(new_node.word)
            dfs(i + 1, j, new_node)            
            dfs(i - 1, j, new_node)
            dfs(i, j + 1, new_node)
            dfs(i, j - 1, new_node)
            visited.remove((i, j))
        
        for i in range(rows):
            for j in range(cols):
                visited = set()
                dfs(i, j, root)

        return list(res)
        