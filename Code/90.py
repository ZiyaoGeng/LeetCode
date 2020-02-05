from typing import List 

class Solution:
	def __init__(self):
		self.lists = []

	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		nums = sorted(nums)
		self.trackback(nums, [], 0)
		return self.lists

	def trackback(self, nums, l, pos):
		self.lists.append(l.copy())
		while pos < len(nums):
			l.append(nums[pos])
			self.trackback(nums, l, pos+1)
			l.pop(-1)
			while pos < len(nums) - 1 and nums[pos] == nums[pos+1]:
				pos += 1
			pos += 1
