from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	max_num, max_i, min_i = nums[0], 1, 1
    	for i in range(len(nums)):
    		if nums[i] < 0:
    			tmp = max_i
    			max_i = min_i
    			min_i = tmp
    		max_i = max(max_i*nums[i], nums[i])
    		min_i = min(min_i*nums[i], nums[i])
    		max_num = max(max_num, max_i)
    	return max_num