# Remove All Adjacent Duplicates in String

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# e repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution(object):
    def remove_duplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)

if __name__ == "__main__":
    s = "azxxzy"
    sol = Solution()

    print(sol.remove_duplicates(s))