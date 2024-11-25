# Custom Sort String

# You are given two strings order and s. 
# All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. 
# More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

#Return any permutation of s that satisfies this property.

class Solution(object):
    def custom_sort_string(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        s_map = {}
        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1
        
        return_str = ""
        for c in order:
            if c in s_map:
                while s_map[c] > 0:
                    return_str += c
                    s_map[c] -= 1
        
        for key, count in s_map.items():
            while count > 0:
                return_str += key
                count -= 1
        
        return return_str
    
if __name__ == "__main__":
    order = "cba"
    s = "abcd"
    solution = Solution()
    print(solution.custom_sort_string(order, s))