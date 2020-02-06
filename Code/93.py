from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def restoreIpAddresses(self, s: str) -> List[str]:
		if len(s) == 0:
			return []
		self.trackback(s, 0, 3)
		return self.lists

	def trackback(self, s: str, pos: int, count: int):
		if count == 0:
			if int(s[pos:]) <= 255:
				if len(s[pos:]) == 1 or (len(s[pos:]) > 1 and s[pos] != '0'):
					self.lists.append(s)
		else:
			for i in range(pos, pos+3):
				if i > pos and s[pos] == '0':
					break
				if int(s[pos: i+1]) <= 255 and count <= len(s[i+1:]) <= count * 3:
					s1 = s[:i+1] + '.' + s[i+1:]
					self.trackback(s1, i+2, count-1)



