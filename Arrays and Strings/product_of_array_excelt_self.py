"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n

        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        
        right_prod = 1
        for j in reversed(range(n)):
            res[j] = res[j] * right_prod
            right_prod *= nums[j]

        return res
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    print(sol.product_except_self(nums))