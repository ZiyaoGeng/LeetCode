
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		matrix = [[1]*n for i in range(m)]
		for i in range(m-1, -1, -1):
			for j in range(n-1, -1, -1):
				if i == m - 1 and j == n -1:
					continue
				elif j == n - 1:
					matrix[i][j] = matrix[i+1][j]
				elif i == m - 1:
					matrix[i][j] = matrix[i][j+1]
				else:
					matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
		return matrix[0][0]

