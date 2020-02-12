from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	ls = [1] * (rowIndex + 1)
    	l, r = 0, 0
    	for i in range(2, rowIndex+2):
    		mid, temp = r // 2, 1

    		while l < mid:
    			ls[l+1] = temp + ls[l+1]
    			ls[r-1] = ls[l+1]
    			temp = ls[l+1] - temp
    			l += 1
    			r -= 1
    		l, r = 0, i
    	return ls
