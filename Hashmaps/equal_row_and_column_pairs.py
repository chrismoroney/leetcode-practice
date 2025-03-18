"""
Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

from collections import defaultdict

class Solution(object):
    def equal_pairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        combos = 0
        hashmap = defaultdict(int)

        for row in grid:
            key = tuple(row)
            hashmap[key] += 1

        for c in range(len(grid[0])):
            col = [grid[r][c] for r in range(len(grid))]
            key = tuple(col)
            if key in hashmap:
                combos += hashmap[key]

        return combos
    
if __name__ == "__main__":
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    solution = Solution()

    print(solution.equal_pairs(grid))