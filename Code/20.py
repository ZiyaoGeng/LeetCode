
class Solution:
    def isValid(self, s: str) -> bool:
    	hashmap = {'(':1,')':-1, '[': 2, ']': -2, '{': 3, '}': -3}
    	arr = []
    	for i in range(len(s)):
    		if len(arr) == 0 or hashmap[s[i]] > 0:
    			arr.append(s[i])
    		elif hashmap[s[i]] < 0:
    			if hashmap[arr[-1]] + hashmap[s[i]] == 0:
    				arr.pop(-1)
    			else:
    				return False
    	if len(arr) !=0:
    		return False
    	else:
    		return True