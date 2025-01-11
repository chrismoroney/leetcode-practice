# Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution(object):
    def max_vowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        total_vowels = 0
        for i in range(k):
            total_vowels += int(s[i] in vowels)

        answer = total_vowels
        
        for i in range(k, len(s)):
            total_vowels += int(s[i] in vowels)
            total_vowels -= int(s[i - k] in vowels)
            answer = max(answer, total_vowels)

        return answer

if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    k = 3
    print(sol.max_vowels(s, k))