from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	if len(nums) == 0:
    		nums.insert(0, target)
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
    	l = l if l < len(nums) else len(nums) - 1
    	if target < nums[l]:
    		nums.insert(l, target)
    		return l
    	else:
    		nums.insert(l + 1, target)
    		return l + 1



