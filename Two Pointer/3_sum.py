"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.two_sum(nums, i, ans)
        return ans
    
    def two_sum(self, nums, i, ans):
        seen = set()
        j = i + 1
        while j < len(nums):
            diff = -nums[i] - nums[j]
            if diff in seen:
                ans.append([nums[i], nums[j], diff])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.three_sum(nums))
        