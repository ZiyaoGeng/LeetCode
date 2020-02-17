
class Solution:
    def trailingZeroes(self, n: int) -> int:
    	sum1 = 0
    	while n >= 5:
    		num, i = 0, 5
    		while i <= n:
    			num = 1 + num * 5
    			i *= 5
    		n -= (i // 5)
    		sum1 += num
    	return sum1