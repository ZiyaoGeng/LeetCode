
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    	num = [0] * (len(num1) + len(num2))
    	for i in range(len(num1)):
    		count = 0
    		for j in range(len(num2)):
    			num3 = int(num1[len(num1)-i-1]) * int(num2[len(num2)-j-1]) + count + num[i+j]
    			num[i+j] = num3 % 10
    			count = num3 // 10
    		if count > 0:
    			num[i+j+1] += count
    	s, flag = '', False
    	for i in range(len(num)):
    		if flag or num[len(num)-1-i] > 0:
    			s += str(num[len(num)-1-i])
    			flag = True
    	return s if len(s) > 0 else '0'

s = Solution()
print(s.multiply("123", "456"))