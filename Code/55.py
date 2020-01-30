from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
    	if len(nums) == 1:
    		return True
    	i,length = len(nums) - 2, len(nums) - 1
    	while i >= 0:
    		if nums[i] + i >= length:
    			length = i 
    		i -= 1
    	return True if length == 0 else False
