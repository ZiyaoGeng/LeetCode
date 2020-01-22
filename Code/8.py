
class Solution:
    def myAtoi(self, str: str) -> int:
    	str = str.lstrip()
    	k = 0
    	for i in range(len(str)):
    		if i == 0 and (str[i] == '-' or str[i] == '+') or \
    		('0' <= str[i] <= '9'):
    			k += 1
    		elif str[i] < '0' or str[i] > '9':
    			break
    	if k == 0 or (k == 1 and (str[0] == '+' or str[0] == '-')):
    		return 0
    	if abs(int(str[:k])) > pow(2, 31) - 1:
    		return - pow(2, 31) if str[0] == '-' else pow(2, 31) - 1
    	return int(str[:k])
