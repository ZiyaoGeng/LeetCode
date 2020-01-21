
class Solution:
    def intToRoman(self, num: int) -> str:
    	hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
    	100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 
    	9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    	s = ""
    	for k in hashmap:
    		if (num // k) != 0:
    			count = num // k
    			num %= k
    			s += hashmap[k] * count
    	return s


