class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        sellPrice = prices[length - 1]
        
        for i in range(length - 2, -1, -1):
            sellPrice = max(sellPrice, prices[i])
            profit = max(profit, sellPrice - prices[i])
            
        return profit