from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	if len(prices) == 0:
    		return 0
    	maxprice = prices[-1]
    	profit = [0] * len(prices)
    	for i in range(len(prices)-2, -1, -1):
    		if maxprice - prices[i] > profit[i+1]:
    			profit[i] = maxprice - prices[i]
    		else:
    			profit[i] = profit[i+1]
    			if maxprice < prices[i]:
    				maxprice = prices[i]
    	return profit[0]