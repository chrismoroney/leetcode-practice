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