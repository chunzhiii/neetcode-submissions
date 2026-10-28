class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def cal_sub_grid_index(i, j):
            return 3 * (i // 3) + j // 3

        look_up = dict()
        n = 9
        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v == '.':
                    continue
                sub_grid_index = cal_sub_grid_index(i, j)
                if v in look_up:
                    existing_info = look_up[v]
                    if i in existing_info[0] or j in existing_info[1] or sub_grid_index in existing_info[2]:
                        return False
                    look_up[v][0].add(i)
                    look_up[v][1].add(j)
                    look_up[v][2].add(sub_grid_index)
                else:
                    look_up[v] = ({i}, {j}, {sub_grid_index})
        return True
