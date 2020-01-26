from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    	l, r = 0, len(nums) - 1
    	while l <= r:
    		mid = (l + r) // 2
    		if nums[mid] == target:
    			mid_l, mid_r = mid, mid
    			while mid_l > l and nums[mid_l - 1] == target:
    				mid_l -= 1
    			while mid_r < r and nums[mid_r + 1] == target:
    				mid_r += 1
    			return [mid_l, mid_r]
    		elif nums[mid] < target:
    			l = mid + 1
    		else:
    			r = mid - 1
    	return [-1, -1]