
class Solution:
    def romanToInt(self, s: str) -> int:
    	maps={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    	results, count = 0, 0
    	char = ''
    	for i in range(len(s)):
    		if i == 0 or count == -1:
    			char = s[i]
    			count =1
    			continue
    		if char == s[i]:
    			count += 1
    		else:
    			if maps[char] < maps[s[i]]:
    				results += maps[s[i]] - maps[char]
    				if i < len(s) - 1:
    					count = -1
    				else:
    					count = 0
    			else:
    				results += count * maps[char]
    				char = s[i]
    				count = 1
    	if count != 0:
    		results += maps[char] * count
    	return results

