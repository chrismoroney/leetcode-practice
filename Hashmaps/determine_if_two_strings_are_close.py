"""
Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""
from collections import defaultdict

class Solution:
    def close_strings(self, word1: str, word2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for c in word1:
            d1[c] += 1

        for c in word2:
            d2[c] += 1

        return sorted(d1.values()) == sorted(d2.values()) and sorted(d1.keys()) == sorted(d2.keys())

if __name__ == "__main__":
    word1 = "cabbba"
    word2 = "abbccc"
    s = Solution()

    print(s.close_strings(word1, word2))