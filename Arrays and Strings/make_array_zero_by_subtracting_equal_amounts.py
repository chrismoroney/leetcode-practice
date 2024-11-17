# Make Array Zero by Subtracting Equal Amounts

# You are given a non-negative integer array nums. In one operation, you must:

# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

class Solution(object):
    def minimum_operations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_of_nums = set(nums)
        if 0 in set_of_nums:
            set_of_nums.remove(0)
        return len(set_of_nums)
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 0, 3, 5]
    print(sol.minimum_operations(nums))