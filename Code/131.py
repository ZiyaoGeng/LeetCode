from typing import List 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
    	ls = []
    	def ispartition(s):
    		i, j = 0, len(s)-1
    		while i < j:
    			if s[i] != s[j]:
    				return False
    			i += 1
    			j -= 1
    		return True

    	def trackback(s, l, pos):
    		if pos == len(s):
    			ls.append(l.copy())
    		else:
    			for i in range(pos, len(s)):
    				if ispartition(s[pos:i+1]):
    					l.append(s[pos:i+1])
    					trackback(s, l, i+1)
    					l.pop(-1)
    	trackback(s, [], 0)
    	return ls