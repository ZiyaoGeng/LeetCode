from typing import List

class Solution:
	def __init__(self):
		self.lists = []	

	def permute(self, nums: List[int]) -> List[List[int]]:
		self.trackback(nums, [0]*len(nums), [])
		return self.lists 

	def trackback(self, nums: List[int], flag: List[int], l: List[int]):
		if  len(l) == len(nums):
			self.lists.append(l.copy())
		else:
			for i in range(0, len(nums)):
				if flag[i] == 0:
					l.append(nums[i])
					flag[i] = 1
					self.trackback(nums, flag, l)
					l.pop(-1)
					flag[i] = 0

s = Solution()
print(s.permute([1]))


