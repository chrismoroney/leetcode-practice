'''
Shortest Word Distance III

Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, 
return the shortest distance between the occurrence of these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.
'''

from typing import List

class Solution:
    def shortest_word_distance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        min_distance = n

        l = -1

        for r in range(n):
            if wordsDict[r] == word1 or wordsDict[r] == word2:
                if l != -1 and (wordsDict[l] != wordsDict[r] or word1 == word2):
                    min_distance = min(min_distance, r - l)
                
                l = r
        
        return min_distance
    
if __name__ == "__main__":
    sol = Solution()
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "makes"

    print(sol.shortest_word_distance(wordsDict, word1, word2))