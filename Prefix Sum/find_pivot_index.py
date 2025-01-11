# Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
# This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution(object):
    def pivot_index(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums):
            if left_sum == (total_sum - left_sum - x):
                return i
            else:
                left_sum += x
        
        return -1
    
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    sol = Solution()
    print(sol.pivot_index(nums))