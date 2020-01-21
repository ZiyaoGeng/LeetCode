
class Solution:
    def convert(self, s: str, numRows: int) -> str:
    	if numRows == 1:
    		return s
    	conv = ""
    	for r in range(numRows):
    		j, flag = r, 1
    		while j < len(s):
    			conv += s[j]
    			if (flag > 0 or r == 0) and r != numRows - 1 :
    				j += (numRows - r - 1) * 2
    			elif flag < 0 or r == numRows - 1:
    				j += r * 2
    			flag = - flag
    	return conv

