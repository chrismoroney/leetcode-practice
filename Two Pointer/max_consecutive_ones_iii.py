# Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution(object):
    def longest_ones(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            
            if k < 0:
                k += 1 - nums[l]
                l += 1

        return r - l + 1
    
if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(sol.longest_ones(nums, k))