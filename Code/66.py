from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    	i, c = len(digits) - 1, 0
    	while i >=0:
    		digits[i] += 1
    		digits[i] %= 10
    		if digits[i] != 0:
    			return digits
    		i -= 1
    	digits.insert(0, 1)
    	return digits
    