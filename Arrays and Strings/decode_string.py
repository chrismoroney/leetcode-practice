"""
Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""

class Solution(object):
    def decode_string(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur_str = ""
        cur_num = 0

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif c == ']':
                prev_str, cnt = stack.pop()
                cur_str = prev_str + (cur_str * cnt)
            else:
                cur_str += c

        return cur_str
    
if __name__ == "__main__":
    sol = Solution()
    s = "3[a]2[bc]"
    s1 = "3[a2[c]]"
    s2 = "2[abc]3[cd]ef"

    print(sol.decode_string(s))
    print(sol.decode_string(s1))
    print(sol.decode_string(s2))