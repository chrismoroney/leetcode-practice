# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution(object):
    def valid_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    print(sol.valid_palindrome(s))