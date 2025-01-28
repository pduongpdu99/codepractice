
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = int('int') % 10**5
        max_price = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_price = max(max_price, profit)
        return max_price