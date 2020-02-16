
class Solution:
    def titleToNumber(self, s: str) -> int:
    	num = 0
    	for i in range(len(s)-1, -1, -1):
    		num += (ord(s[i]) - 64) * pow(26, len(s)-1-i)
    	return num
