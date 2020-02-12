from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    	if numRows == 0:
    		return []
    	ls = [[1]]
    	for i in range(1, numRows):
    		former = ls[-1]
    		latter = [1] * (len(former) + 1)
    		l, r = 0, len(former) - 1
    		while l < r:
    			latter[l+1] = former[l] + former[l+1]
    			latter[r] = latter[l+1]
    			l += 1
    			r -= 1
    		ls.append(latter)
    	return ls