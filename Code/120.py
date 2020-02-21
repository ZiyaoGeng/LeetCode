from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
    	if len(triangle) == 0:
    		return 0
    	minload = triangle[-1].copy()
    	for i in range(len(triangle)-2, -1, -1):
    		for j in range(len(minload)):
    			if j <= i:
    				minload[j] = triangle[i][j] + min(minload[j], minload[j+1])

    	return minload[0]


print(Solution().minimumTotal([
]))