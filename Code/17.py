from typing import List

class Solution:
	def __init__(self):
		self.ls = []
		self.hashmap = {
    	1: [""],
    	2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 
    	5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 
    	8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
    	}

	def letterCombinations(self, digits: str) -> List[str]:
		if len(digits) == 0 or (len(digits) == 1 and digits[0] == '1'):
			return []
		for i in range(len(self.hashmap[int(digits[0])])):
			self.dfs(self.hashmap[int(digits[0])][i], digits, 1)
		return self.ls

	def dfs(self, s: str, l: List[str], j: int) -> List[str]:
		if j >= len(l):
			self.ls.append(s)
		else:	
			for i in range(len(self.hashmap[int(l[j])])):
				self.dfs(s+self.hashmap[int(l[j])][i], l, j + 1)


