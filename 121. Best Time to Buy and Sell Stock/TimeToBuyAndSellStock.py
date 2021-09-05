class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for stock in prices:
            if buy > stock:
                buy = stock
            if profit < stock-buy:
                profit = stock-buy
        return profit
