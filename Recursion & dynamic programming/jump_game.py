# Jump Game

# You are given an integer array nums. 
# You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def can_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0
    
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    nums1 = [3, 2, 1, 0, 4]
    sol = Solution()
    print(sol.can_jump(nums))
    print(sol.can_jump(nums1))
