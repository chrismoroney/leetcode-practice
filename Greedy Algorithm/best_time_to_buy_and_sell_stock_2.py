# Best Time To Buy And Sell Stock II
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        i = 0
        valleys = prices[0]
        peaks = prices[0]
        max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valleys = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peaks = prices[i]
            max_profit += peaks - valleys
        
        return max_profit
    
if __name__ == "__main__":
    sol = Solution()
    stocks = [7, 1, 5, 3, 6, 4]
    print(sol.max_profit(stocks))
