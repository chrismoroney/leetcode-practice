'''
Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest substring that contains at most two distinct characters.
'''

from collections import defaultdict

class Solution:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        hashmap = defaultdict()

        l, r = 0, 0

        max_len = 2

        while r < n:
            hashmap[s[r]] = r
            r += 1

            if len(hashmap) == 3:
                idx = min(hashmap.values())
                del hashmap[s[idx]]
                l = idx + 1

            max_len = max(max_len, r - l)

        return max_len
    
if __name__ == "__main__":
    sol = Solution()
    s = "HeLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOOOOOOOOOO WWWWOOOOORRRRLLLLLLLLLLLLLLDDDDDDDDDD"
    print(sol.length_of_longest_substring_two_distinct(s))
