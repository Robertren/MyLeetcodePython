class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

        # profit = 0
        # for i in xrange(len(prices)-1):
        #     for j in xrange(i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]
        # return profit
        
        # if len(prices) == 0 or len(prices) == 1 :
        #      return 0
        # # count = 0 
        # # while prices[count] >= prices[count + 1] and count < len(prices) - 2:
        # #     count += 1
        # #     print count
        # # if max(prices[count+1:]) - min(prices[0:count+1]) < 0:
        # #     return 0
        # # else: return max(prices[count+1:]) - min(prices[0:count+1]) 
        # from operator import itemgetter
        # index = min(enumerate(prices), key=itemgetter(1))[0]
        # if len(prices[index + 1:]) != 0:
        #     return max(prices[index+1:]) - prices[index]
        # else: return 0
