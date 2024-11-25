# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.

class Solution(object):
    def get_max_len(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        positive, negative = 0, 0
        for num in nums:
            if num == 0:
                positive = 0
                negative = 0
                continue
            elif num > 0:
                positive += 1
                negative += 1 if negative != 0 else 0
            elif num < 0:
                tmp = positive + 1
                positive = negative + 1 if negative != 0 else 0
                negative = tmp
            if positive > answer:
                answer = positive
        return answer
                
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,-2,-3,-4]
    print(sol.get_max_len(nums))