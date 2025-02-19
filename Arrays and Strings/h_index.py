'''
H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
'''

class Solution(object):
    def h_index(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        ans = 0

        while (ans < len(citations) and citations[len(citations) - 1 - ans] > ans):
            ans += 1
        
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    citations = [3, 0, 6, 1, 5]

    print(sol.h_index(citations))