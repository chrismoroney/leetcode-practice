# Problem: Number of Islands
# You are given a 2D grid map of '1's (land) and '0's (water). 
# Your task is to count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are surrounded by water.

def num_of_islands(grid: list[list[str]])-> int:
    if not grid:
        return 0

    num_islands = 0

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return
        
        grid[r][c] = 0

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dfs(r, c)
                num_islands += 1

    return num_islands

if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ]

    print(num_of_islands(grid))