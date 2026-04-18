from typing import List

class Solution:
    # Time Complexity: O(n*m) where n is the amount and m is the number of coins
    # Space Complexity: O(n) where n is the amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a dp array of size amount + 1 and initialize it with amount + 1 (a value greater than any possible number of coins)
        # We do this because we want to find the minimum number of coins, and initializing with a large value allows us to easily compare and update the dp array
        # It would look like this: dp = [8, 8, 8, 8, 8, 8, 8, 8] for amount = 7 and coins = [1, 2, 3]
        # It doesn't matter what value we choose as long as it's greater than the maximum number of coins we could possibly need (which is amount itself if we use all coins of denomination 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0: #Diff
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    """
                    coin = 4
                    a = 7
                    dp[7] = 1 + dp[7 - 4] --> 1 + dp[3]
                    """
        return dp[amount] if dp[amount] != amount + 1 else -1 # Default Value else -1 for not possible