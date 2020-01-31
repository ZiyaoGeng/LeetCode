
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
    	f = self.factorial(n)
    	s = ""
    	l = [i for i in range(1, n+1)]
    	for i in range(0, n):
    		k %= f
    		f /= n - i
    		s += str(self.helps(f, k, l))
    	return s

    def factorial(self, n):
    	num = 1
    	while n >0 :
    		num *= n
    		n -= 1
    	return num

    def helps(self, f: int, k: int, l) -> str:
    	c = int((k - 1) // f)
    	num = l.pop(c)
    	return num
