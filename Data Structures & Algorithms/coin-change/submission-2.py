class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # not making it amount + 1, introduces a bug. Say amount is 7, we want to dp to be 0-7, not 0 - 6.
        dp  = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a],  1 + dp[a-c])
        
        return dp[amount] if dp[amount]!= amount + 1 else -1

    