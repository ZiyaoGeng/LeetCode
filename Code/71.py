
class Solution:
    def simplifyPath(self, path: str) -> str:
    	stack = []
    	s, w= "", ""
    	i = 1
    	while 0 < i < len(path):
    		if path[i] == '/':
    			i += 1
    			continue
    		while i < len(path) and path[i] != '/':
    			w += path[i]
    			i += 1
    		if len(w) > 0:
    			if w == '..':
    				if len(stack) > 0:
    					stack.pop(-1)
    			elif w != '.':
    				stack.append(w)
    			w = ""
    	for i in range(len(stack)-1, -1, -1):
    		s = '/' + stack[i] + s
    	return s if len(s) > 0 else "/"