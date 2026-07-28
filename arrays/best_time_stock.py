class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top_profit = 0
        prev_buy = 0
        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):
                if prices[i] > prev_buy:
                    prev_buy = prices[i]
                if prices[j] > prices[i]:
                    top_profit = prices[j] - prices[i]
            
        return top_profit