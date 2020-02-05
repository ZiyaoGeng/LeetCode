from typing import List 

class Solution:
	def __init__(self):
		self.lists = [0]

	def grayCode(self, n: int) -> List[int]:
		flag = [0] * pow(2, n)
		flag[0] = 1
		self.trackback(n, ['0'] * n, flag, 0, 1)
		i, j = 0, len(self.lists) - 1
		return self.lists

	def trackback(self, n: int, l: List[str], flag: List[int], pos: int, f: 0):
		if len(self.lists) == pow(2, n) or pos < 0 or pos >= len(l):
			return
		while pos >= 0 and pos < len(l):
			l[pos] = '0' if l[pos] == '1' else '1'
			num = int("".join(l), 2)
			if flag[num] == 0:
				self.lists.append(num)
				flag[num] = 1
				if f == 0:
					self.trackback(n, l, flag, len(l)-pos, 1)
				else:
					self.trackback(n, l, flag, len(l)-pos-1, 0)
			else:
				l[pos] = '0' if l[pos] == '1' else '1'
				if f == 0:
					pos += 1
				else:
					pos -= 1
