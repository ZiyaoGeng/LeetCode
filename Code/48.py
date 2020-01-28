from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    	for i in range(len(matrix)):
    		for j in range(i+1, len(matrix[0])):
    			temp = matrix[i][j]
    			matrix[i][j] = matrix[j][i]
    			matrix[j][i] = temp
    	for i in range(len(matrix)):
    		for j in range(len(matrix[0])//2):
    			temp = matrix[i][j]
    			matrix[i][j] = matrix[i][len(matrix[0])-j-1]
    			matrix[i][len(matrix[0])-j-1] = temp