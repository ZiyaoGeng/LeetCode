
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    	num = [0] * (len(num1) + len(num2))
    	for i in range(len(num1)):
    		n1 = int(num1[len(num1)-i-1])
    		for j in range(len(num2)):
    			n2 = int(num2[len(num2)-j-1])
    			n3 = n1*n2 + num[i+j]
    			num[i+j] = n3 % 10
    			num[i+j+1] += n3 // 10
    	s, flag = '', False
    	for i in range(len(num)):
    		if flag or num[len(num)-1-i] > 0:
    			s += str(num[len(num)-1-i])
    			flag = True
    	return s if len(s) > 0 else '0'