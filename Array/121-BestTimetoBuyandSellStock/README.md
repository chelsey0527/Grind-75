# Best Time to Buy and Sell Stock

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)!

### [Solution 1](/Array/121-BestTimetoBuyandSellStock/solutionTP.py): Two Pointer

```javascript
const maxProfit = (prices) => {
    let left = 0; // Buy
    let right = 1; // sell
    let maxProfit = 0;
    while (right < prices.length) {
        if (prices[left] < prices[right]) {
            let profit = prices[right] - prices[left]; // our current profit

            maxProfit = Math.max(maxProfit, profit);
        } else {
            left = right;
        }
        right++;
    }
    return maxProfit;
};
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)


