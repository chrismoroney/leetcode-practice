"""
Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows

"""

class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        if num_rows == 1:
            return s

        res = []
        n = len(s)
        chars_per_grouping = (num_rows - 1) * 2

        for row in range(num_rows):
            idx = row
            while idx < n:
                res.append(s[idx])

                if not (row == 0 or row == num_rows - 1):
                    chars_fill = chars_per_grouping - 2 * row
                    second_idx = idx + chars_fill

                    if second_idx < n:
                        res.append(s[second_idx])
                
                idx += chars_per_grouping

        return "".join(res)
        
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    num_rows = 4
    solution = Solution()

    print(solution.convert(s, num_rows))