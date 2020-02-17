
class Solution:
    def reverseBits(self, n: int) -> int:
    	nums = 0
    	for i in range(31, -1, -1):
    		if 1 << i <= n:
    			nums += 1 << 31 - i
    			wn -= 1 << i
    	return nums 