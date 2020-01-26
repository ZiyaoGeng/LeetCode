
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    	count, flag = 0, 1 if (dividend > 0 and divisor > 0) or \
    	(dividend < 0 and divisor < 0) else -1
    	dividend, divisor = abs(dividend), abs(divisor)
    	num, add = divisor, 1
    	while True:
    		while dividend - num >= 0:
    			count += add
    			dividend -= num
    			num += num
    			add += add
    		if dividend - divisor >= 0:
    			add = 1
    			num = divisor
    		else:
    			break
    	if count == 1 << 31 and flag > 0:
    		count -= 1
    	return count * flag