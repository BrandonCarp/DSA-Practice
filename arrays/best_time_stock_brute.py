from typing import List

# Best Time to Buy & Sell Stock — https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Brute force: check every buy/sell pair
# Time: O(n²) — nested loops, ~n²/2 pairs | Space: O(1)
# Verdict: correct (199/212) but TLE at n≈10⁵ — needs O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):
                if prices[j] - prices[i] > top_profit:
                    top_profit = prices[j] - prices[i]
            
        return top_profit