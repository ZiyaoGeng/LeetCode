from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    	stack = []
    	for i in tokens:
    		if i.isdigit() or i[1:].isdigit():
    			stack.append(int(i))
    		else:
    			n1 = stack.pop(-1)
    			n2 = stack.pop(-1)
    			if i == '+':
    				stack.append(n1 + n2)
    			elif i == '-':
    				stack.append(n2 - n1)
    			elif i == '*':
    				stack.append(n1 * n2)
    			else:
    				stack.append(int(n2 / n1))
    	return stack[0]

print(-1//6)