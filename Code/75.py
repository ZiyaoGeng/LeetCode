from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
    	l, r, i = 0, len(nums)-1, 0
    	while i <= r:
    		if nums[i] == 0:
    			nums[i] = 1
    			nums[l] = 0
    			l += 1
    		elif nums[i] == 2:
    			temp = nums[r]
    			nums[r] = 2
    			nums[i] = temp
    			r -= 1
    			continue
    		i += 1