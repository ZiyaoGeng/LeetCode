from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	j = 0
    	for i in range(len(nums)):
    		num = target - nums[i]
    		if num in nums[i+1:]:
    			j = nums[i+1:].index(num) + i + 1
    			break
    	return [i, j]
