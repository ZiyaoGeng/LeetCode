from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    	if len(matrix) == 0 or len(matrix[0]) == 0:
    		return False
    	r = len(matrix[0]) - 1
    	for i in range(len(matrix)):
    		if matrix[i][0] > target:
    			return False
    		if matrix[i][0] <= target and matrix[i][r] >= target:
    			l = 0
    			while l <= r:
    				mid = (l + r) 
    				if matrix[i][mid] == target:
    					return True
    				elif matrix[i][mid] > target:
    					r = mid - 1
    				else:
    					l = mid + 1
    			return False
    	return False

