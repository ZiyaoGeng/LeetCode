from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    	lists = []
    	nums = sorted(nums)
    	for i in range(len(nums)-2):
    		if i > 0 and nums[i] == nums[i-1]:
    			continue
    		l, r = i + 1, len(nums) - 1
    		while l < r:
    			if nums[i] + nums[l] + nums[r] == 0:
    				lists.append([nums[i], nums[l], \
    					nums[r]])
    				while l < r and nums[l] == nums[l+1]:
    					l += 1
    				while l < r and nums[r] == nums[r-1]:
    					r -= 1
    				l += 1
    				r -= 1
    			elif nums[i] + nums[l] + nums[r] < 0:
    				l += 1
    			else:
    				r -= 1
    	return lists
