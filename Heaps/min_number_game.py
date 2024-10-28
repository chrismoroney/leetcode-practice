# Minimum Number Game

# You are given a 0-indexed integer array nums of even length and there is also an empty array arr. 
# Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
# Now, first Bob will append the removed element in the array arr, and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.

from heapq import heapify, heappop

class Solution():
    def minimum_number_game(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []

        heapify(nums)

        while nums:
            alice = heappop(nums)
            bob = heappop(nums)
            arr.append(bob)
            arr.append(alice)
        
        return arr


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 4, 2, 3]
    
    print(sol.minimum_number_game(nums))