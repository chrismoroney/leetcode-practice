# Greatest Common Divisor of Strings

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution(object):
    def gcd_of_strings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        if str1 + str2 != str2 + str1:
            return ""

        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
        
if __name__ == "__main__":
    sol = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"
    print(sol.gcd_of_strings(str1, str2))