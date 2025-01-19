# Gas Station

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
# You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
# If there exists a solution, it is guaranteed to be unique.

class Solution(object):
    def can_complete_circuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        total_gain, sub_gain, answer = 0, 0, 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            sub_gain += gas[i] - cost[i]

            if sub_gain < 0:
                sub_gain = 0
                answer = i + 1
        
        return answer if total_gain >= 0 else -1
    

if __name__ == "__main__":
    sol = Solution()
    # Completes at index 3
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    # not possible, can only start at index 2 then travel to either index 0 or 1, but don't have enough gas to come back
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]

    print(sol.can_complete_circuit(gas, cost))
    print(sol.can_complete_circuit(gas2, cost2))
    