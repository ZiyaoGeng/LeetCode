from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		candidates = sorted(candidates)
		self.dfs(candidates, target, [], 0)
		return self.lists


	def dfs(self, candidates: List[int], target: int, l: List[int], pos: int):
		if target == 0:
			self.lists.append(l.copy())
		else:
			for i in range(pos, len(candidates)):
				if target - candidates[i] >= 0:
					l.append(candidates[i])
					self.dfs(candidates, target-candidates[i], l, i)
					l.pop(len(l)-1)
				else:
					break