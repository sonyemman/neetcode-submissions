# prices = [10,1,5,6,7,1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list_min = prices[0]
        max_profit = 0

        for price in prices: 
            if price < list_min:
                list_min = price
            max_profit = max(max_profit, price - list_min)
        
        return max_profit