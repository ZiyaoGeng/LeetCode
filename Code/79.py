from typing import List

class Solution:
	def __init__(self):
		self.flag = False

	def exist(self, board: List[List[str]], word: str) -> bool:
		matrix = [[0]*len(board[0]) for _ in range(len(board))]
		for r in range(len(board)):
			for c in range(len(board[0])):
				if board[r][c] == word[0]:
					matrix[r][c] = 1
					self.trackback(board, matrix, word, 1, r, c)
					if self.flag == True:
						return True
					else:
						matrix[r][c] = 0
		return False

	def trackback(self, board: List[List[str]], matrix: List[List[int]], word: str, pos: int, r: int, c: int):
		if pos == len(word):
			self.flag = True
		else:
			if self.flag == True:
				return True
			if r > 0 and matrix[r-1][c] == 0 and word[pos] == board[r-1][c]:
				matrix[r-1][c] = 1
				self.trackback(board, matrix, word, pos+1, r-1, c)
				matrix[r-1][c] = 0
			if c < len(board[0]) - 1 and matrix[r][c+1] == 0 and word[pos] == board[r][c+1]:
				matrix[r][c+1] = 1
				self.trackback(board, matrix, word, pos+1, r, c+1)
				matrix[r][c+1] = 0
			if r < len(board) - 1 and matrix[r+1][c] == 0 and word[pos] == board[r+1][c]:
				matrix[r+1][c] = 1
				self.trackback(board, matrix, word, pos+1, r+1, c)
				matrix[r+1][c] = 0
			if c > 0 and matrix[r][c-1] == 0 and word[pos] == board[r][c-1]:
				matrix[r][c-1] = 1
				self.trackback(board, matrix, word, pos+1, r, c-1)
				matrix[r][c-1] = 0
