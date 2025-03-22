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
        stairs = [0] * (n + 1)
        return self.memoization(0, n, stairs)

    def memoization(self, i, n, stairs):
        if i > n:
            return 0
        if i == n:
            return 1
        if stairs[i] > 0:
            return stairs[i]
        stairs[i] = self.memoization(i + 1, n, stairs) + self.memoization(i + 2, n, stairs)

        return stairs[i]

if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.climb_stairs(n))