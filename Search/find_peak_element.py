# Find Peak Element

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
# return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. 
# In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

class Solution(object):
    def find_peak_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        
        return low

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,1,3,5,6,4]
    print(solution.find_peak_element(nums))