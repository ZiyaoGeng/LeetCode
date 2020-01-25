from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    	lists = [] 
    	nums = sorted(nums)
    	print(nums)
    	for i in range(len(nums)-3):
    		if i > 0 and nums[i] == nums[i-1]:
    			continue
    		min1 = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
    		if min1 > target:
    			continue
    		max1 = nums[i] + nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3]
    		if max1 < target:
    			continue
    		for j in range(i+1, len(nums)-2):
    			if j > i + 1 and nums[j] == nums[j-1]:
    				continue
    			l = j + 1
    			r = len(nums) - 1
    			while l < r:
    				num = nums[i] + nums[j] + nums[l] + nums[r]
    				if num == target:
    					lists.append([nums[i], nums[j], nums[l], nums[r]])
    					while l < r and nums[l] == nums[l+1]:
    						l += 1
    					while l < r and nums[r] == nums[r-1]:
    						r -= 1
    					l += 1
    					r -= 1
    				elif num < target:
    					l += 1
    				else:
    					r -= 1
    	return lists

