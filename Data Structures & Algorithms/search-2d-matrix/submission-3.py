class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            mRow = (top + bottom) // 2

            if matrix[mRow][-1] < target:
                top = mRow + 1
            elif matrix[mRow][0] > target:
                bottom = mRow - 1
            else:
                break
        
        if not top <= bottom:
            return False
        
        l, r = 0, COLS - 1

        mRow = (top + bottom) // 2

        while l <= r:
            m = (l + r) // 2

            if matrix[mRow][m] < target:
                l = m + 1
            elif matrix[mRow][m] > target:
                r = m - 1
            else:
                return True
        return False