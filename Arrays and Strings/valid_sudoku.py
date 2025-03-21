"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9

        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    continue

                idx = int(board[r][c]) - 1

                if rows[r][idx] == 1:
                    return False
                rows[r][idx] = 1

                if cols[c][idx] == 1:
                    return False
                cols[c][idx] = 1

                box = (r // 3) * 3 + c // 3
                if boxes[box][idx] == 1:
                    return False
                boxes[box][idx] = 1
        
        return True
    
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    sol = Solution()

    print(sol.is_valid_sudoku(board))