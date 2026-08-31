# coins = [1,5,10]

'''
DP solution 
memo[amount] = min number of coins to add to that amount 
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxInt = 100000000
        memo = [maxInt] * (amount + 1)
        memo[0] = 0

        for amount in range(1, amount + 1): 
            for coin in coins: 
                if amount - coin >= 0: 
                    memo[amount] = min(memo[amount], 1 + memo[amount - coin])

        return memo[amount] if memo[amount] != maxInt else -1


        
        