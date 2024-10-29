# Minimum String Length After Removing Substrings

# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

class Solution(object):
    def min_length(self, s):
        """
        :type s: str
        :rtype: int
        """

        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB", "")

            if "CD" in s:
                s = s.replace("CD", "")
        
        return len(s)

if __name__ == "__main__":
    sol = Solution()
    s = "ABFCACDB"

    print(sol.min_length(s))