from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def generateParenthesis(self, n: int) -> List[str]:
		self.dfs(n, "", 0, 0)
		return self.lists

	def dfs(self, n: int, s: str, l: int, r: int):
		if len(s) == n * 2:
			self.lists.append(s)
		else:
			if l < n:
				self.dfs(n, s+"(", l + 1, r)
			if r < n and r < l:
				self.dfs(n, s+")", l, r + 1)