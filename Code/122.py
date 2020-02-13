from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	if len(prices) == 0:
    		return 0
    	profit = [0] * len(prices)
    	for i in range(len(prices)-2, -1, -1):
    		if prices[i] < prices[i+1]:
    			profit[i] = profit[i+1] + prices[i+1] - prices[i]
    		else:
    			profit[i] = profit[i+1]
    	return profit[0]
