# Word Subsets

# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.

class Solution(object):
    def word_subsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """

        def count_word(w):
            c_arr = [0] * 26
            for c in w:
                c_arr[ord(c) - ord('a')] += 1
            return c_arr

        b_arr = [0] * 26
        for b in words2:
            for idx, cnt in enumerate(count_word(b)):
                b_arr[idx] = max(b_arr[idx], cnt)
        
        ans = []
        for a in words1:
            if all(x >= y for x, y in zip(count_word(a), b_arr)):
                ans.append(a)
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["l","e"]
    print(sol.word_subsets(words1, words2))