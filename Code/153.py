from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
    	l, r = 0, len(nums)-1
    	while l < r - 1:
    		mid = (l + r) // 2
    		if nums[l] <= nums[mid] and nums[r] < nums[l]:
    			l = mid 
    		else:
    			r = mid 
    	return min(nums[l], nums[r])