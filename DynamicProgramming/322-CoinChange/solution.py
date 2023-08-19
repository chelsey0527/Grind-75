class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Initialize dp array with the amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Brute force to run through every amount and coins to store
        for a in range(1, amount + 1):
            for c in coins:
                print('a:', a, ', c:', c)
                # If c is part of the a
                if a - c >= 0:
                    print(dp[a], dp[a - c] + 1)
                    # Find the smallest combination for every number before amount
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    print('new dp',a,':', dp[a])
                print('---')
                print(dp)
                print('---')

        return dp[amount] if dp[amount] != amount + 1 else -1