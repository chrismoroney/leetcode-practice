# Palindrome Permutation

# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

class Solution(object):
    def can_permute_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        freq_map = {}
        num_odd_chars = 0

        for c in s:
            if c not in freq_map:
                freq_map[c] = 1
            else:
                freq_map[c] += 1
        
        for key, val in freq_map.items():
            if val % 2 != 0:
                num_odd_chars += 1
                if num_odd_chars >= 2:
                    return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    pal = "aab"
    non_pal = "code"
    print(sol.can_permute_palindrome(pal))
    print(sol.can_permute_palindrome(non_pal))