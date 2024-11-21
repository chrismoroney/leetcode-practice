# Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque

class Solution(object):
    def oranges_rotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(grid), len(grid[0])
        current_time = 0

        # up, down, left, right
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        queue = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append(((x, y), current_time))
        
        while queue:
            fruit_location, time = queue.popleft()
            current_time = time
            
            x, y = fruit_location
            
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if grid[new_x][new_y] == 1:
                        queue.append(((new_x, new_y), time + 1))
                        grid[new_x][new_y] = 2

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return -1

        return current_time
    
if __name__ == "__main__":
    grid = [
        [2, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 2, 1]
    ]
    solution = Solution()
    print(solution.oranges_rotting(grid))