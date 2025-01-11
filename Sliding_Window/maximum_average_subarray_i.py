# Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution(object):
    def find_max_average(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        answer = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            answer = max(answer, window_sum)
        
        return answer/float(k)
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4

    print(sol.find_max_average(nums, k))
