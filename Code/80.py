from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	if len(nums) == 0:
    		return 0
    	flag = True
    	l = 0
    	for i in range(1, len(nums)):
    		if nums[l] != nums[i]:
    			l += 1
    			nums[l] = nums[i]
    			flag = True
    		elif nums[l] == nums[i] and flag == True:
    			l += 1
    			nums[l] = nums[i]
    			flag = False
    	return l + 1
