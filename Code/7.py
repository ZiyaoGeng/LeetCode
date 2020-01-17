
class Solution:
	# 1
    def reverse(self, x: int) -> int:
    	s, s1 = str(x), ""
    	for i in range(len(s)):
    		if i == 0 and s[len(s)-i-1] == '0' and len(s) > 1:
    			continue
    		if i == len(s)-1 and s[len(s)-i-1] == '-':
    			s1 = s[len(s)-i-1] + s1
    		else:
    			s1 += s[len(s) - i - 1]
    	if abs(float(s1)) > pow(2, 31) - 1:
    		return 0
    	return int(s1)

    # 2
	def reverse(self, x: int) -> int:
		rev = 0
		abs_x = abs(x)
		while abs_x != 0:
			pop = abs_x % 10
			abs_x //= 10
			if rev > (pow(2, 31) - 1)/10:
				return 0
			rev = rev * 10 + pop
		if x < 0:
			rev = -rev
		return rev
