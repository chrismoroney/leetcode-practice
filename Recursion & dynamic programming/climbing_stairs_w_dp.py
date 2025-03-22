"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.climb_stairs(n))