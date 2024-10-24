# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
# Given the current state of the m x n grid board, return the next state.

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def count_live_neighbors(row, col):
            live_neighbors = 0
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and abs(board[new_row][new_col]) == 1:
                    live_neighbors += 1
            return live_neighbors
        
        for r in range(rows):
            for c in range(cols):
                status = board[r][c]
                live_neighbors = count_live_neighbors(r, c)

                if status == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                
                if status == 0 and live_neighbors == 3:
                    board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                status = board[r][c]
                if status > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

if __name__ == "__main__":
    solution = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution.gameOfLife(board)
    print(board)