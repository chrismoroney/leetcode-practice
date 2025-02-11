# Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

class Solution(object):
    def longest_subarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = 0
        longest = 0
        left = 0

        for right in range(len(nums)):
            zeros += 1 if nums[right] == 0 else 0

            while zeros > 1:
                zeros -= 1 if nums[left] == 0 else 0
                left += 1
            
            longest = max(longest, right - left)

        return longest

if __name__ == "__main__":
    sol = Solution()

    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(sol.longest_subarray(nums))