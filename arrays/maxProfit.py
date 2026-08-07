from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        topProfit = 0
        bestBuy = prices[0]
        for price in prices:
            if price - bestBuy > topProfit:
                topProfit = price - bestBuy
            if price < bestBuy:
                bestBuy = price

        return topProfit
