from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def combine(self, n: int, k: int) -> List[List[int]]:
		self.trackback(n, k, [], 1)
		return self.lists

	def trackback(self, n: int, k: int, l: List[int], pos: int):
		if len(l) == k:
			self.lists.append(l.copy())
		else:
			for i in range(pos,n+1):
				l.append(i)
				self.trackback(n, k, l, i+1)
				l.pop(-1)