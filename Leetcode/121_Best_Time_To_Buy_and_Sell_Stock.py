from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left=buy right=sell | These are INDICES not literal prices
        maxP = 0

        # While the right pointer isn't at the end
        while r < len(prices):
            # Profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # Because r is at a position lower than l is right now
            r += 1
        return maxP
    
    def maxProfit_two(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return int(max_profit)