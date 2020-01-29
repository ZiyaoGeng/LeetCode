from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		nums = sorted(nums)
		self.backtrack(nums, [0]*len(nums), [])
		return self.lists

	def backtrack(self, nums: List[int], flag: List[int], l: List[int]):
		if len(nums) == len(l):
			self.lists.append(l.copy())
		else:
			i = 0
			while i < len(nums):
				if flag[i] == 0:
					l.append(nums[i])
					flag[i] = 1
					self.backtrack(nums, flag, l)
					l.pop(-1)
					flag[i] = 0
					while i < len(nums)-1 and nums[i] == nums[i+1]:
						i += 1
				i += 1