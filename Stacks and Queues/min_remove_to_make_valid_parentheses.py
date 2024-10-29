# Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution(object):
    def min_remove_to_make_valid(self, s):
        """
        :type s: str
        :rtype: str
        """
        index_to_keep = set()
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) != 0:
                    stack_idx = stack.pop()
                    index_to_keep.add(stack_idx)
                    index_to_keep.add(i)
            else:
                index_to_keep.add(i)

        return_str = ""
        for i in range(len(s)):
            if i in index_to_keep:
                return_str += s[i]
        
        return return_str

if __name__ == "__main__":
    sol = Solution()
    s = "lee(t(c)o)de)"
    print(sol.min_remove_to_make_valid(s))