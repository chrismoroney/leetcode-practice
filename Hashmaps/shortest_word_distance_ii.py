"""
Shortest Word Distance II

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
"""

from typing import List
from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashmap = defaultdict(list)
        self.n = len(wordsDict)

        for i in range(self.n):
            self.hashmap[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min_distance = self.n - 1

        word_1_list = self.hashmap[word1]
        word_2_list = self.hashmap[word2]

        for i in word_1_list:
            for j in word_2_list:
                min_distance = min(min_distance, abs(i - j))

        return min_distance
    
if __name__ == "__main__":
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"

    wd = WordDistance(wordsDict)

    print(wd.shortest(word1, word2))