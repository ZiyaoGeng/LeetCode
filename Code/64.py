from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
    	m, n = len(grid), len(grid[0])
    	min_len = [[0] * n for _ in range(m)]
    	for i in range(m):
    		for j in range(n):
    			if i == 0 and j == 0:
    				min_len[i][j] = grid[i][j]
    			elif i == 0:
    				min_len[i][j] = min_len[i][j-1] + grid[i][j]
    			elif j == 0:
    				min_len[i][j] = min_len[i-1][j] + grid[i][j]
    			else:
    				min_len[i][j] = min(min_len[i-1][j], min_len[i][j-1]) + grid[i][j]
    	return min_len[m-1][n-1]
