class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minBuy = prices[0] 

        for sell in prices: 
            maxProfit = max(maxProfit, sell - minBuy)
            #update min at that point 
            minBuy = min(minBuy, sell)
        
        return maxProfit
        