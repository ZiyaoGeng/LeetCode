from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    	if len(matrix) == 0:
    		return []
    	l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    	i, j = 0, 0
    	nums = []
    	while True:
    		while j <= r:
    			nums.append(matrix[i][j])
    			j += 1
    		j -= 1
    		t += 1
    		i = t
    		if t > b:
    			break
    		while i <= b:
    			nums.append(matrix[i][j])
    			i += 1
    		i -= 1
    		r -= 1
    		j = r
    		if l > r:
    			break
    		while j >= l:
    			nums.append(matrix[i][j])
    			j -= 1
    		j += 1
    		b -= 1
    		i = b
    		if t > b:
    			break
    		while i >= t:
    			nums.append(matrix[i][j])
    			i -= 1
    		i += 1
    		l += 1
    		j = l
    		if l > r:
    			break
    	return nums