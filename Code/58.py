
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    	if len(s) == 0:
    		return 0
    	s = s.rstrip()
    	arr = s.split(' ')
    	return len(arr[-1])