# Reverse Only Letters

# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0
        right = len(s) - 1

        while left <= right:
            left_char = s[left]
            right_char = s[right]

            if left_char.isalpha() and right_char.isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif left_char.isalpha() and not right_char.isalpha():
                right -= 1
            elif not left_char.isalpha() and right_char.isalpha():
                left += 1
            else:
                left += 1
                right -= 1
        
        return ''.join(s)


if __name__ == "__main__":
    solution = Solution()
    s = "a-bC-dEf-ghIj--klMn-o-p-Q-R-sTuVW-XyZ-"
    new_s = solution.reverseOnlyLetters(s)
    print(new_s)