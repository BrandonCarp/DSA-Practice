from typing import List

# Best Time to Buy & Sell Stock — https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
   # One pass, two carried values: best_buy (a price), top_profit (a difference)
   # Time: O(n) — one loop, O(1) work per lap | Space: O(1) — two variables regardless of n
   # Traced on paper first. 212/212, beats 95.85%.

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
