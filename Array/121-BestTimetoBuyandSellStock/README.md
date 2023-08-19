# Best Time to Buy and Sell Stock

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)!

### [Solution 1](/Array/121-BestTimetoBuyandSellStock/solution.py)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        profit = 0

        for i in range(len(prices)):
            minBuy = min(minBuy, prices[i])
            profit = max(profit, prices[i] - minBuy)

        return profit

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)


