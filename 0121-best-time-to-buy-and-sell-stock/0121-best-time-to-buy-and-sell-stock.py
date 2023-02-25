class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0 #maxProfit
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:#cp is less than sp
                max_profit =max(currentProfit,max_profit) #Since cp is less than sp so t could be one of outcome
            else:
                left = right #co > sp so we will now consider sp as cp
            right += 1 #checking for new sp 
        return max_profit