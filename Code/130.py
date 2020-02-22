from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
    	if len(board) == 0:
    		return
    	flag = True
    	n, m = len(board), len(board[0])
    	flagmatrix = [[0] * m for i in range(n)]
    	def helper(board, i, j, ans):
    		nonlocal flag
    		if (i == 0 or i == n-1 or j == 0 or \
    			j == m-1) and board[i][j] == 'O':
    			flag = False
    			return 
    		elif board[i][j] == 'X':
    			return
    		else:
    			if flagmatrix[i][j] == 0:
    				ans.append([i, j])
    				flagmatrix[i][j] = 1
    				helper(board, i+1, j, ans)
    				helper(board, i-1, j, ans)
    				helper(board, i, j+1, ans)
    				helper(board, i, j-1, ans)
    	
    	for i in range(1, n):
    		for j in range(1, m):
    			if board[i][j] == 'O' and flagmatrix[i][j] == 0:
    				ans = []
    				helper(board, i, j, ans)
    				if flag == True:
    					for [a, b] in ans:
    						board[a][b] = 'X'
    				flag = True
