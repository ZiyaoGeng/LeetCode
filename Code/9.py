class Solution:
	# 1
    def isPalindrome(self, x: int) -> bool:
    	if x < 0:
    		return False
    	temp, lens, count = x, 1, 0
    	while temp >= 10:
    		temp //= 10
    		lens += 1
    	temp = x
    	while temp != 0:
    		i = temp // pow(10, lens-1-count)
    		j = temp % 10
    		temp %= pow(10, lens-1-count)
    		temp //= 10
    		if i != j:
    			return False
    		count += 2
    	return True

    # 2
	def isPalindrome(self, x: int) -> bool:
		if x < 0 or (x%10==0 and x!=0):
			return False
		rev = 0
		while rev < x:
			rem = x % 10
			x //= 10
			rev = rev * 10 + rem
		if rev == x or rev//10 == x:
			return True
		else:
			return False
