# Perform String Shifts

# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [directioni, amounti]:

# directioni can be 0 (for left shift) or 1 (for right shift).
# amounti is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

from collections import deque

class Solution(object):
    def string_shift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        
        s_list = list(s)
        s_q = deque()
        for c in s_list:
            s_q.append(c)

        for i in range(len(shift)):
            d = shift[i][0]
            a = shift[i][1]

            for j in range(a):
                if d == 0:
                    char = s_q.popleft()
                    s_q.append(char)
                else:
                    char = s_q.pop()
                    s_q.appendleft(char)

        return ''.join(s_q)
        
if __name__ == "__main__":
    sol = Solution()
    s = "abcdefg"
    shift = [[1,1],[1,1],[0,2],[1,3]]
    print(sol.string_shift(s, shift))