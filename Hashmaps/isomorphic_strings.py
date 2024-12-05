# Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.


class Solution(object):
    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map_to_t = {}
        t_map_to_s = {}
        
        for c_s, c_t in zip(s, t):
            if c_s not in s_map_to_t and c_t not in t_map_to_s:
                s_map_to_t[c_s] = c_t
                t_map_to_s[c_t] = c_s

            elif s_map_to_t.get(c_s) != c_t or t_map_to_s.get(c_t) != c_s:
                return False
        return True

        

if __name__ == "__main__":
    sol = Solution()
    str1 = "paper"
    str2 = "title"

    print(sol.is_isomorphic(str1, str2))