class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        profit = 0

        for i in range(len(prices)):
            minBuy = min(minBuy, prices[i])
        profit = max(profit, prices[i] - minBuy)

        return profit
