from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def subsets(self, nums: List[int]) -> List[List[int]]:
		self.trackback(nums, [], 0)
		return self.lists

	def trackback(self, nums : List[int], l: List[int], pos: int):
		self.lists.append(l.copy())
		for i in range(pos, len(nums)):
			l.append(nums[i])
			self.trackback(nums, l, i+1)
			l.pop(-1)