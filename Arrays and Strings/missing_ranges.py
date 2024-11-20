# Missing Ranges

# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, 
# where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
# That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

class Solution(object):
    def find_missing_ranges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        n = len(nums)

        if n == 0:
            return [[lower, upper]]

        return_list = []
        if lower < nums[0]:
            return_list.append([lower, nums[0] - 1])

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            return_list.append([nums[i] + 1, nums[i + 1] - 1])
        
        if upper > nums[n - 1]:
            return_list.append([nums[n - 1] + 1, upper])
        
        return return_list
    
if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 3, 50, 75]
    lower, upper = 0, 99
    print(solution.find_missing_ranges(nums, lower, upper))
