# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

class Solution(object):
    # Sort each word, then determine if in an existing list in dictionary. O(n log n)
    def group_anagrams_slower(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for s in strs:
            sorted_s = sorted(s)
            key = ''.join(sorted_s)

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        return list(anagrams.values())

    # Create a map of all letters, mark the number of that character there is in an array of size 26, then insert that array into a dictionary if it doesn't exists,
    # and insert the word into the list as a value in the hashmap. O(n)
    def group_anagrams_faster(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
         
        char_to_index = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 
            'h': 7, 'i': 8, 'j': 9, 'k': 10, 
            'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
            'q': 16, 'r': 17, 's': 18, 
            't': 19, 'u': 20, 'v': 21,
            'w': 22, 'x': 23, 
            'y': 24, 'z': 25
        }

        for s in strs:
            char_count = [0] * 26

            for c in s:
                idx = char_to_index[c]
                char_count[idx] += 1
            
            key = tuple(char_count)
            anagrams[key].append(s)
        
        return list(anagrams.values())

    

if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    #print(sol.group_anagrams_slower(strs))
    print(sol.group_anagrams_faster(strs))