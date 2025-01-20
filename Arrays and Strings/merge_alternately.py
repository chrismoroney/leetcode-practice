# Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution(object):
    def merge_alternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        n, m = len(word1), len(word2)
        new_str = []

        while i < n or j < m:
            if i < n:
                new_str += word1[i]
                i += 1
            if j < m:
                new_str += word2[j]
                j += 1

        return ''.join(new_str)
    
if __name__ == "__main__":
    sol = Solution()
    word1 = "ab"
    word2 = "pqrs"
    print(sol.merge_alternately(word1, word2))