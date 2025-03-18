"""
Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. 
You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. 
An exit is defined as an empty cell that is at the border of the maze. 
The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

"""

from collections import deque

class Solution(object):
    def nearest_exit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        rows, cols = len(maze), len(maze[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            x, y, distance = q.popleft()

            for cx, cy in dirs:
                dx, dy = x + cx, y + cy

                if 0 <= dx < rows and 0 <= dy < cols and maze[dx][dy] == '.':
                    if (dx == 0 or dx == rows-1 or dy == 0 or dy == cols-1) and not (dx, dy) == (entrance[0], entrance[1]):
                        return distance + 1
                    else:
                        maze[dx][dy] = '+'
                        q.append((dx, dy, distance + 1))

        
        return -1
    
if __name__ == "__main__":
    maze1 = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance1 = [1,2]

    maze2 = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance2 = [1,0]

    sol = Solution()

    print(sol.nearest_exit(maze1, entrance1))
    print(sol.nearest_exit(maze2, entrance2))
    