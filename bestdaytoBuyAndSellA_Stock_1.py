class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        i = 0
        j = 1
        while i < len(prices) and j < len(prices):
            if prices[j] - prices[i] <= 0 :
                i = j
            elif prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i] 
            j+=1            

        return max_profit
        
