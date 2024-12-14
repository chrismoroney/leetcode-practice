# Find Good Days to Rob the Bank

# You and a gang of thieves are planning on robbing a bank. 
# You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. 
# The days are numbered starting from 0. You are also given an integer time.

# The ith day is a good day to rob the bank if:

# There are at least time days before and after the ith day,
# The number of guards at the bank for the time days before i are non-increasing, and
# The number of guards at the bank for the time days after i are non-decreasing.
# More formally, this means day i is a good day to rob the bank if and only if security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

# Return a list of all days (0-indexed) that are good days to rob the bank. 
# The order that the days are returned in does not matter.

class Solution(object):
    def good_days_to_rob_bank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        if time == 0:
            return [i for i in range(len(security))]

        n = len(security)
        non_increasing = [0] * n
        non_decreasing = [0] * n

        # Calculate non-increasing streaks
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1
                print(non_increasing)
        print()

        # Calculate non-decreasing streaks
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1
                print(non_decreasing)

        good_days = []
        for i in range(time, n - time):
            if non_increasing[i] >= time and non_decreasing[i] >= time:
                good_days.append(i)
        
        return good_days
    
if __name__ == "__main__":
    security = [5,3,3,3,5,6,2]
    time = 2
    solution = Solution()

    print(solution.good_days_to_rob_bank(security, time))