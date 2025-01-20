# Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n, m = len(s), len(t)

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == n

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.is_subsequence(s, t))