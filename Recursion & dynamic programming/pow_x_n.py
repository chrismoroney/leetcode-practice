# Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution(object):
    def my_pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def binary_exponintation(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1.0 / binary_exponintation(x, -n)
            
            if n % 2 == 1:
                return x * binary_exponintation(x * x, (n-1) // 2)
            else:
                return binary_exponintation(x * x, n//2)
        
        return binary_exponintation(x, n)

if __name__ == "__main__":
    solution = Solution()
    x = 2
    n = 100
    print(solution.my_pow(x, n))