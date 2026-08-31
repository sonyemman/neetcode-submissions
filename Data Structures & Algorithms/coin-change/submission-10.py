class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1D - DP solution 
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0 

        for amount in range(1, amount + 1): 
            for coin in coins: 
                if amount - coin >= 0: 
                    # found an answer 
                    memo[amount] = min(memo[amount], 1 + memo[amount - coin])
        return memo[amount] if memo[amount] != amount + 1 else -1