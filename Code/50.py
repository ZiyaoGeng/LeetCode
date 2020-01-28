
class Solution:
    def myPow(self, x: float, n: int) -> float:
    	if n < 0:
    		x = 1 / x
    		n = - n
    	res, a, b = 1, 1, x
    	while a <= n:
    		if a << 1 > n:
    			res *= b
    			n -= a
    			a = 1
    			b = x
    		else:
    			a = a << 1
    			b *= b
    	return res