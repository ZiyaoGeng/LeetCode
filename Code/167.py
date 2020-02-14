from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	ans = {}
    	for i, num in enumerate(numbers):
    		if ans.get(target - num) != None:
    			return [ans.get(target - num), i+1]
    		ans[num] = i + 1
    