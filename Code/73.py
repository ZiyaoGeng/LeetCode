from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    	r, c = [0]*len(matrix), [0]*len(matrix[0])
    	for i in range(len(matrix)):
    		for j in range(len(matrix[0])):
    			if matrix[i][j] == 0:
    				r[i] = 1
    				c[j] = 1
    	for i in range(len(matrix)):
    		if r[i] == 1:
    				matrix[i] = [0] * len(matrix[0])
    		for j in range(len(matrix[0])):
    			if c[j] == 1:
    				matrix[i][j] = 0
