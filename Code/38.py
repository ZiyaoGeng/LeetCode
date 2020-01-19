
class Solution:
    def countAndSay(self, n: int) -> str:
    	if n == 1:
    		return "1"
    	return self.func(self.countAndSay(n-1))
    
    def func(self, s: str) -> str:
    	ch, s1, count = s[0], "", 1
    	for i in range(1, len(s)):
    		if ch == s[i]:
    			count += 1
    		else:
    			s1 += str(count) + ch
    			ch = s[i]
    			count = 1
    	s1 += str(count) + ch
    	return s1


s = Solution()
print(s.countAndSay(5))

    	