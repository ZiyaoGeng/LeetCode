from typing import List 


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
    	l, r = 0, len(nums) - 1
    	while l <= r:
    		while l < r and nums[l] == nums[r]:
    			l += 1
    		mid = (l + r) // 2
    		if nums[mid] == target:
    			return True
    		if nums[mid] < target:
    			if nums[l] <= target and nums[l] > nums[mid]:
    				r = mid - 1
    			else:
    				l = mid + 1
    		if nums[mid] > target:
    			if nums[r] >= target and nums[r] < nums[mid]:
    				l = mid + 1
    			else:
    				r = mid - 1
    	return False

print(Solution().search([1,3,1,1], 1))