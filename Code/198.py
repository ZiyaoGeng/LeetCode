from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
    	if len(nums) == 0:
    		return 0
    	if len(nums) == 1:
    		return nums[0]
    	for i in range(len(nums)-2, -1, -1):
    		if i == len(nums) - 2:
    			nums[i] = max(nums[-1], nums[-2])
    		else:
    			nums[i] = max(nums[i+1], nums[i+2] + nums[i])
    	return nums[0]