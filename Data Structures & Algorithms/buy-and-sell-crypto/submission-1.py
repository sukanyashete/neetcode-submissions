class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            #if prices[i] > buy:
            #    profit = max(profit, prices[i] - buy)
            #else:
            #    buy = prices[i]
            #instead of above if-else it can also be written as this:
            buy = min(buy, prices[i])
            profit = max(profit, prices[i] - buy)
        return profit