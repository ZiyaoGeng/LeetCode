
class Solution:
    def addBinary(self, a: str, b: str) -> str:
    	i, j, c, s = len(a)-1, len(b)-1, 0, ""
    	while True:
    		if i < 0 and j < 0:
    			break
    		num1 = int(a[i]) if i >=0 else 0
    		num2 = int(b[j]) if j >=0 else 0
    		s = str((num1 + num2 + c) % 2)+ s
    		c = (num1 + num2 + c) // 2
    		i -= 1
    		j -= 1
    	s = "1" + s if c > 0 else s
    	return s

