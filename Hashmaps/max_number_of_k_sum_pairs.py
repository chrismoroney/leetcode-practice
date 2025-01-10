# Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

from collections import defaultdict

class Solution(object):
    def max_operations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = defaultdict(int)
        ans = 0

        for num in nums:
            comp = k - num

            if hash_map[comp] > 0:
                hash_map[comp] -= 1
                ans += 1
            else:
                hash_map[num] += 1

        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 1, 3, 4, 3]
    k = 6
    print(sol.max_operations(nums, k))