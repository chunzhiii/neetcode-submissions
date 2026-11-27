class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j, index):
            print(i, j, index)
            if index == len(word):
                return True
            if (i, j) in visited or (i < 0 or i >= rows) or (j < 0 or j >= cols) or (board[i][j] != word[index]):
                return False
            visited.add((i, j))
            flag = dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1)
            visited.remove((i, j))
            return flag
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
