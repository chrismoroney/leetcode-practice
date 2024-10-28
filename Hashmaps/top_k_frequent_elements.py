# Top K Frequent Numbers

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from heapq import heappush, heappop

class Solution():
    # O(n) solution total 
    # O(n) to traverse through nums and insert elements into hash map
    # O(n) to traverse through hash map and find top k items
    # O(n) to pop all of the top k items
    def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        return_list = []
        nums_dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        top_k_items = []

        for key, val in nums_dict.items():
            heappush(top_k_items, (key, val))
            if len(top_k_items) > k:
                heappop(top_k_items)
        
        while top_k_items:
            return_list.append(heappop(top_k_items)[1])

        return return_list

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(sol.top_k_frequent(nums, k))