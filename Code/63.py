from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    	m, n = len(obstacleGrid), len(obstacleGrid[0])
    	obstacleGrid = [[i*-1 for i in j] for j in obstacleGrid]
    	for i in range(m-1, -1, -1):
    		for j in range(n-1, -1, -1):
    			if obstacleGrid[i][j] == -1:
    				obstacleGrid[i][j] = 0
    			elif i == m-1 and j == n-1:
    				obstacleGrid[i][j] = 1
    			elif j == n - 1:
    				obstacleGrid[i][j] = obstacleGrid[i+1][j]
    			elif i == m - 1:
    				obstacleGrid[i][j] = obstacleGrid[i][j+1]
    			else:
    				obstacleGrid[i][j] = obstacleGrid[i+1][j]+ obstacleGrid[i][j+1]
    	return obstacleGrid[0][0]