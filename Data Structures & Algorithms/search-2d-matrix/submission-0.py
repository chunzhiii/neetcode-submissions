class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) - 1
        while l_row <= r_row:
            mid_row = l_row + (r_row - l_row) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = matrix[mid_row]
                l_col, r_col = 0, len(target_row) - 1
                while l_col <= r_col:
                    mid_col = l_col + (r_col - l_col) // 2
                    if target_row[mid_col] == target:
                        return True
                    elif target_row[mid_col] < target:
                        l_col = mid_col + 1
                    else:
                        r_col = mid_col - 1
                return False
            elif matrix[mid_row][0] > target:
                r_row = mid_row - 1
            else:
                l_row = mid_row + 1
                
        return False
