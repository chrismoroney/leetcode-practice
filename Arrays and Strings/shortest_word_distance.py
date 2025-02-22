"""
Shortest Word Distance

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
"""

from typing import List

class Solution:
    def shortest_distance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        min_distance = n - 1

        w_1_idx = -1
        w_2_idx = -1

        for i in range(n):
            if wordsDict[i] == word1:
                w_1_idx = i
            elif wordsDict[i] == word2:
                w_2_idx = i
            
            if w_1_idx != -1 and w_2_idx != -1:
                min_distance = min(min_distance, abs(w_1_idx - w_2_idx))
        
        return min_distance

if __name__ == "__main__":
    sol = Solution()
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"

    print(sol.shortest_distance(wordsDict, word1, word2))