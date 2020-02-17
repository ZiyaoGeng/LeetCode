from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    	def rotate(nums: List[int]):
    		l, r = 0, len(nums)-1
    		while l < r:
    			temp = nums[l]
    			nums[l] = nums[r]
    			nums[r] = temp
    			l += 1
    			r -= 1
    		return nums
    	if len(nums) == 0:
    		return
    	k %= len(nums)
    	nums[:-k] = rotate(nums[:-k])
    	nums[-k:] = rotate(nums[-k:])
    	rotate(nums)