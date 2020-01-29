from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
    	i = len(nums) - 2
    	while i >= 0 and nums[i + 1] <= nums[i]:
    		i -= 1
    	if i >= 0:
    		j = len(nums) - 1
    		while j >= 0 and nums[j] <= nums[i]:
    			j -= 1
    		temp = nums[i]
    		nums[i] = nums[j]
    		nums[j] = temp
    	self.reverse(nums, i+1)

    def reverse(self, nums: List[int], start: int):
    	i, j = start, len(nums) - 1
    	while i < j:
    		temp = nums[i]
    		nums[i] = nums[j]
    		nums[j] = temp
    		i += 1
    		j -= 1