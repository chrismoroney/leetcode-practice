# Minimum Cost Homecoming of a Robot in a Grid

# There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. 
# You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol).
# You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).

# The robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. 
# Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.

# If the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].
# If the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].
# Return the minimum total cost for this robot to return home.

from typing import List

def min_cost(start_pos: List[int], home_pos: List[int], row_costs: List[int], col_costs: List[int]) -> int:
    """
    :type startPos: List[int]
    :type homePos: List[int]
    :type rowCosts: List[int]
    :type colCosts: List[int]
    :rtype: int
    """
    start_row, start_col = start_pos
    home_row, home_col = home_pos

    total_cost = 0

    if start_row < home_row:
        for i in range(start_row + 1, home_row + 1):
            total_cost += row_costs[i]
    else:
        for j in range(start_row - 1, home_row - 1, -1):
            total_cost += row_costs[j]

    if start_col < home_col:
        for i in range(start_col + 1, home_col + 1):
            total_cost += col_costs[i]
    else:
        for j in range(start_col - 1, home_col - 1, -1):
            total_cost += col_costs[j]
    
    return total_cost

if __name__ == "__main__":
    start_pos = [1, 0] 
    home_pos = [2, 3]
    row_costs = [5, 4, 3]
    col_costs = [8, 2, 6, 7]
    print(min_cost(start_pos, home_pos, row_costs, col_costs))