# Max Consecutive Ones III

# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution(object):
    def longest_ones(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]

            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1

if __name__ == "__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    solution = Solution()
    print(solution.longest_ones(nums, k))
        