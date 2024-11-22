# Number of Ways to Select Buildings

# You are given a 0-indexed binary string s which represents the types of buildings along a street where:

# s[i] = '0' denotes that the ith building is an office and
# s[i] = '1' denotes that the ith building is a restaurant.
# As a city official, you would like to select 3 buildings for random inspection. 
# However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

# For example, given s = "001101", 
# we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
# Return the number of valid ways to select 3 buildings.

class Solution(object):
    def number_of_ways(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeroes, ones, count01, count10, ans = 0, 0, 0, 0, 0

        for c in s:
            if c == '0':
                zeroes += 1
                count10 += ones
                ans += count01
            else:
                ones += 1
                count01 += zeroes
                ans += count10
        
        return ans
    
if __name__ == "__main__":
    s = '001101'
    s1 = '001010001001110101110100'

    solution = Solution()
    print(solution.number_of_ways(s))
    print(solution.number_of_ways(s1))
