
class Solution:
    def convertToTitle(self, n: int) -> str:
    	s = ""
    	while n > 0:
    		c = n % 26 if n % 26 != 0 else 26
    		n = n // 26 if c != 26 else n // 26 - 1
    		s = chr(64+c) + s
    	return s