from typing import List 

class Solution:
	def __init__(self):
		self.lists = [0]

	def grayCode(self, n: int) -> List[int]:
		flag = [0] * pow(2, n)
		flag[0] = 1
		self.trackback(n, ['0'] * n, flag, 0)
		return self.lists

	def trackback(self, n: int, l: List[str], flag: List[int], pos: int):
		if len(self.lists) == pow(2, n) or pos < 0 or pos >= len(l):
			return
		l[pos] = '0' if l[pos] == '1' else '1'
		num = int("".join(l), 2)
		if flag[num] == 0:
			self.lists.append(num)
			flag[num] = 1
			self.trackback(n, l, flag, pos-1)
			self.trackback(n, l, flag, pos+1)

l = Solution().grayCode(3)
print(l)