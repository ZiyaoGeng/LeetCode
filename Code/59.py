from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    	lists = [[0] * n for i in range(n)]
    	l, r, t, b = 0, n - 1, 0, n - 1
    	i, j, count = 0, 0, 1
    	while l <= r and t <= b:
    		while j < r:
    			lists[i][j] = count
    			count += 1
    			j += 1
    		t += 1
    		while i < b:
    			lists[i][j] = count
    			count += 1
    			i += 1
    		r -= 1
    		while j > l:
    			lists[i][j] = count
    			count += 1
    			j -= 1
    		b -= 1
    		while i > t:
    			lists[i][j] = count
    			count += 1
    			i -= 1
    		l += 1
    	if n % 2 == 1:
    		lists[n//2][n//2] = count
    	else:
    		lists[n//2][n//2-1] = count
    	return lists
