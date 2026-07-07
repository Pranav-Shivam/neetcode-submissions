class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       left = prices[0]
       max_profit = 0

       for num in prices[1:]:
        if left > num:
            left = num
        profit = num - left
        if max_profit < profit:
            max_profit = profit
       return max_profit
       

