from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	ans = {}
    	for i, num in enumerate(numbers):
    		if ans.get(target - num) != None:
    			return [ans.get(target - num), i+1]
    		ans[num] = i + 1


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	l, r = 0, len(numbers) - 1
    	while l < r:
    		if numbers[l] + numbers[r] == target:
    			return [l, r]
    		elif numbers[l] + numbers[r] > target:
    			r -= 1
    		else:
    			l += 1