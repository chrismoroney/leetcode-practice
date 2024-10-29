# Minimum String Length After Removing Substrings

# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.


# This problem was also done in the Arrays and Strings section, but this is optimized to use a stack
class Solution(object):
    def min_length(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= 2:
                if (stack[-2] == "A" and stack[-1] == "B") or stack[-2] == "C" and stack[-1] == "D":
                    stack.pop()
                    stack.pop()
        
        return len(stack)
        

if __name__ == "__main__":
    sol = Solution()
    s = "ABFCACDB"

    print(sol.min_length(s))