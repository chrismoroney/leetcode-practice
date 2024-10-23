#Shortest Path in a Binary Matrix
# You are given an n x n binary matrix grid. 
# The matrix contains only 0s (empty cells) and 1s (blocked cells). 
# You need to find the shortest path from the top-left corner (0,0) to the bottom-right corner (n-1,n-1). 
# You can only move in 8 possible directions (up, down, left, right, and diagonals).

# If there is no path, return -1.

# Constraints:
# You cannot move through a blocked cell (1).
# You cannot move outside the grid boundaries.
# The start and destination cells must be empty (0).

from collections import deque

def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    n = len(grid)

    # if start/end is blocked then not possible
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    movement = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1)]

    queue = deque([(0,0,1)])

    grid[0][0] = 1

    while queue:
        x, y, distance = queue.popleft()

        if x == n-1 and y == n-1:
            return distance
        else:
            for change_x, change_y in movement:
                new_x = x + change_x
                new_y = y + change_y

                if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, distance + 1))

    return -1

if __name__ == "__main__":
    grid = [
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0]
    ]
    
    print(shortestPathBinaryMatrix(grid))