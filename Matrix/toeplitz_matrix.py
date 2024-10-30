# Toeplitz Matrix

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
# Example
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true

class Solution(object):
    def is_toeplitz_matrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        def check_diagonal(x, y):
            value = matrix[x][y]
            while x < len(matrix) and y < len(matrix[0]):
                if value != matrix[x][y]:
                    return False
                x += 1
                y += 1
            
            return True
        

        for i in range(len(matrix)):
            if not check_diagonal(i, 0):
                return False

        for j in range(len(matrix[0])):
            if not check_diagonal(0, j):
                return False             
                
        return True

if __name__ == "__main__":
    sol = Solution()
    # returns True
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(sol.is_toeplitz_matrix(matrix))

    # returns False
    matrix = [[1,2],[2,2]]
    print(sol.is_toeplitz_matrix(matrix))

    
