from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	if len(nums) == 0:
    		return 0
    	l, r = 0, len(nums) - 1
    	while l <= r:
    		mid = (l + r) // 2
    		if nums[mid] < target:
    			l = mid + 1
    		elif nums[mid] > target:
    			r = mid - 1
    		elif nums[mid] == target:
    			return mid
    	if l < len(nums) and target > nums[l]:
    		return l + 1
    	else:
    		return l 



