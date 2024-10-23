# Problem: Word Search
# You are given an m x n grid of characters and a string word. 
# Your task is to find out if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in the construction of the word.

# Write a function that returns true if the word exists in the grid, and false otherwise.

def exist(board: list[list[str]], word: str) -> bool:

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[idx] != board[r][c]:
            return

        temp = board[r][c]
        board[r][c] = '#'      

        found = dfs(r-1, c, idx+1) or dfs(r+1, c, idx+1) or dfs(r, c-1, idx+1) or dfs(r, c+1, idx+1)

        board[r][c] = temp

        return found

    rows, cols = len(board), len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(r, c, 0):
                    return True

    return False

if __name__ == "__main__":
    board = [
        ['A','B','C','E','F','G'],
        ['S','F','C','S','H','I'],
        ['A','D','E','E','J','K'],
        ['M','N','O','P','Q','R'],
        ['S','T','U','V','W','X']
    ]
    word1 = "ABCDECS"    # False
    word2 = "SEE"        # True
    word3 = "XYZ"        # False
    word4 = "ABCEFSJ"    # False
    word5 = "ABCDEFGHIJKLMNOPQRSTUVWX" # False
    word6 = "MNOPE"      # True

    print(exist(board, word6))