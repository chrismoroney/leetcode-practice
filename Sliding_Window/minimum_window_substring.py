"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

from collections import Counter, defaultdict

class Solution(object):
    def min_window(self, s, t):
        target_count = Counter(t)
        required_chars = len(target_count)
        window_count = defaultdict(int)
        current_chars = 0
        left = 0
        min_len = float("inf")
        min_start = 0

        for right, char in enumerate(s):
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                current_chars += 1
            
            while current_chars == required_chars:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                window_count[s[left]] -= 1
                if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                    current_chars -= 1

                left += 1

        return s[min_start: min_start + min_len] if min_len != float("inf") else ""
    

if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.min_window(s, t))