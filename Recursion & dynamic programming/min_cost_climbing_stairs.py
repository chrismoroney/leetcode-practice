"""
Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

from typing import List

class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            one_step = min_cost[i-1] + cost[i-1]
            two_steps = min_cost[i-2] + cost[i-2]

            min_cost[i] = min(one_step, two_steps)

        return min_cost[-1]
    
if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    s = Solution()
    print(s.min_cost_climbing_stairs(cost))