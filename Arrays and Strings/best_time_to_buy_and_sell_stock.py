# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        i = 0
        j = i + 1
        while j < len(prices):
            current_profit = prices[j] - prices[i]
            if current_profit > 0:
                max_profit = max(current_profit, max_profit)
            else:
                i = j
            j += 1

        return max_profit
    
if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.max_profit(prices))