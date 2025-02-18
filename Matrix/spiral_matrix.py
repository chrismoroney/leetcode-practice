# Spiral Matrix

'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution(object):
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0

        bool_matrix = [[0] * cols for _ in range(rows)]
        VISITED = 1

        x = 0
        y = 0
        result = []

        for _ in range(rows * cols):
            result.append(matrix[x][y])
            bool_matrix[x][y] = VISITED
            
            dx = x + dirs[current_direction][0]
            dy = y + dirs[current_direction][1]

            if not (0 <= dx < rows and 0 <= dy < cols and bool_matrix[dx][dy] == 0):
                current_direction = (current_direction + 1) % 4
                dx, dy = x + dirs[current_direction][0], y + dirs[current_direction][1]

            x, y = dx, dy

        return result
    
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiral_order(matrix))