from typing import List

# Best Time to Buy & Sell Stock — https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# One pass, two carried values: best_buy (a price), top_profit (a difference)
# Time: O(n) — one loop, O(1) work per lap | Space: O(1) — two variables regardless of n
# Traced on paper first. 212/212, beats 95.85%.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top_profit = 0
        best_buy = prices[0]
        for price in prices:
            if price - best_buy > top_profit:
                top_profit = price - best_buy
            if price < best_buy:
                best_buy = price

        return top_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))     
    print(s.maxProfit([7, 6, 4, 3, 1]))        
    print(s.maxProfit([2, 1, 2, 1, 0, 1, 2])) 