
class Solution:
    def numDecodings(self, s: str) -> int:
    	if len(s) == 0:
    		return 0
    	nums = [0] * len(s)
    	for i in range(len(s)-1, -1, -1):
    		if s[i] == '0':
    			nums[i] = 0
    		elif i == len(s) - 1:
    			nums[i] = 1
    		elif int(s[i:i+2]) <= 26:
    			if i == len(s) - 2:
    				nums[i] = nums[i+1] + 1
    			else:
    				nums[i] = nums[i+1] + nums[i+2]
    		else:
    			nums[i] = nums[i+1]
    	return nums[0]