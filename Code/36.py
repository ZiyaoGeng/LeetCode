from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    	ans = {}
    	for i in range(len(board)):
    		for j in range(len(board)):
    			if board[i][j].isdigit():
    				n = int(board[i][j])
    				if not self.isValid(n, i, ans):
    					return False
    				if not self.isValid(n, 9+j, ans):
    					return False
    				if not self.isValid(n, (i//3)*3+(j//3)+18, ans):
    					return False
    				
    	return True
    					
    def isValid(self, n: int, pos: int, ans):
    	if ans.get(pos) is None:
    		ans[pos] = [0] * 10
    		ans[pos][n] = 1
    	else:
    		if ans[pos][n] == 1:
    			return False
    		else:
    			ans[pos][n] = 1
    	return True