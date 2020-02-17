

class Solution:
    def hammingWeight(self, n: int) -> int:
    	c = 0
    	for i in range(31, -1, -1):
    		if n >= 1 << i:
    			n -= 1 << i
    			c += 1
    	return c