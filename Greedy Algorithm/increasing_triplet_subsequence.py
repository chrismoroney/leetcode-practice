'''
Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices 
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''

class Solution(object):
    def increasing_triplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        a = float("inf")
        b = float("inf")

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
    
if __name__ == "__main__":
    nums = [2, 1, 5, 0, 4, 6]
    sol = Solution()
    print(sol.increasing_triplet(nums))