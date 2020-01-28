from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		candidates = sorted(candidates)
		self.dfs(candidates, target, [], 0)
		return self.lists

	def dfs(self, candidates: List[int], target: int, l: List[int], pos: int):
		if target == 0:
			if l.copy() not in self.lists:
				self.lists.append(l.copy())
		else:
			for i in range(pos, len(candidates)):
				if target - candidates[i] >= 0:
					l.append(candidates[i])
					self.dfs(candidates, target - candidates[i], l, i + 1)
					l.pop(len(l) - 1)
				else:
					break

s = Solution()
print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))