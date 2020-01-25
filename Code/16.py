from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
    	clost = nums[0] + nums[1] + nums[2]
    	nums = sorted(nums)
    	for i in range(len(nums)-2):
    		if i > 0 and nums[i] == nums[i-1]:
    			continue
    		l = i + 1
    		r = len(nums) - 1
    		while l < r:
    			num = nums[i] + nums[l] + nums[r]
    			if num - target == 0:
    				return target
    			if abs(num - target) < abs(clost - target):
    				clost = num
    			if num - target < 0:
    				while l < r and nums[l] == nums[l+1]:
    					l += 1
    				l += 1
    			else:
    				while l < r and nums[r] == nums[r-1]:
    					r -= 1
    				r -= 1
    	return clost
