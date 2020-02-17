
class Solution:
    def reverseBits(self, n: int) -> int:
    	nums = 0
    	for i in range(32, -1, -1):
    		if 1 << i <= n:
    			nums += 1 << 31 - i
    			n -= 1 << i
    	return nums