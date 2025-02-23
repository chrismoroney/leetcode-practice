'''
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''

from collections import Counter

class Solution(object):
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        target_count = Counter(t)
        required_chars = len(target_count)
        window_count = {}
        have = 0 

        l = 0
        min_len = float("inf")
        min_start = 0 

        for r, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] == target_count[char]:
                have += 1

            while have == required_chars:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                window_count[s[l]] -= 1
                if s[l] in target_count and window_count[s[l]] < target_count[s[l]]:
                    have -= 1
                
                l += 1

        return s[min_start:min_start + min_len] if min_len != float("inf") else ""

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()

    print(sol.min_window(s, t))