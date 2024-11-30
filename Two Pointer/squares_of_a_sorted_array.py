# Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sorted_squares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                val = nums[right]
                right -= 1
            else:
                val = nums[left]
                left += 1
            squares[i] = val ** 2
        return squares
    
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    sol = Solution()

    print(sol.sorted_squares(nums))