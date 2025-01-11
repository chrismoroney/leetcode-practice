# Removing Starts From a String

# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


class Solution(object):
    def remove_stars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)
        

if __name__ == "__main__":
    sol = Solution()

    s = "leet**cod*e"
    s1 = "erase*****"

    print(sol.remove_stars(s))
    print(sol.remove_stars(s1))