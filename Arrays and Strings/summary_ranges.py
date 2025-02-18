# Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

class Solution(object):
    def summary_ranges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        right = 0

        while right < len(nums):
            left = nums[right]

            while right + 1 < len(nums) and nums[right] + 1 == nums[right + 1]:
                right += 1
            
            if left != nums[right]:
                ranges.append(str(left) + '->' + str(nums[right]))
            else:
                ranges.append(str(nums[right]))

            right += 1

        return ranges
    
if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    print(sol.summary_ranges(nums))
