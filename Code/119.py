from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	ls = [1] * (rowIndex + 1)
    	for i in range(1, rowIndex+1):
    		l, r, temp,  = 0, i, 1
    		while l < i // 2:
    			ls[l+1] = temp + ls[l+1]
    			ls[r-1] = ls[l+1]
    			temp = ls[l+1] - temp
    			l += 1
    			r -= 1
    	return ls

print(Solution().getRow(5))