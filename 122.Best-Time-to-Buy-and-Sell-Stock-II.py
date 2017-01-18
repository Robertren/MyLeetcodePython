class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0 or length ==  1:
            return 0
        buy_price = prices[0]
        profit = 0 
        for i in range(length):
            if prices[i] > buy_price:
                profit += prices[i] - buy_price
                buy_price = prices[i]
                
            if prices[i] < buy_price:
                buy_price = prices[i]
        return profit
            