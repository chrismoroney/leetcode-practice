# Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List

def minSubArrayLen(target: int, nums: List[int]):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """

    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
        
    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    print(minSubArrayLen(target, nums))