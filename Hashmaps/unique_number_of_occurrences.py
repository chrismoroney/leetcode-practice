# Unique Number of Occurences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

from collections import defaultdict

class Solution(object):
    def unique_occurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_map = defaultdict(int)

        for val in arr:
            arr_map[val] += 1

        set_of_vals = set()
        for v in arr_map.values():
            if v not in set_of_vals:
                set_of_vals.add(v)
            else:
                return False

        return True
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(sol.unique_occurrences(arr))