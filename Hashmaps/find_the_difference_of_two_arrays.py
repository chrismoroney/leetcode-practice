# Find the Difference of Two Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

class Solution(object):
    def find_difference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        def elementFoundInOneList(l1, l2):
            s = set()
            return_list = set()

            for num in l2:
                s.add(num)

            for num in l1:
                if num not in s: return_list.add(num)

            return list(return_list)

        return [elementFoundInOneList(nums1, nums2), elementFoundInOneList(nums2, nums1)]
    

if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    sol = Solution()

    print(sol.find_difference(nums1, nums2))