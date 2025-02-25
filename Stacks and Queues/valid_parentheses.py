"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        p_map = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in p_map.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != p_map[c]:
                    return False

        return not stack
    
if __name__ == "__main__":
    s = "([({()})])"
    sol = Solution()
    print(sol.is_valid(s))