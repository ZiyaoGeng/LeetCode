from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	ans = {}
    	for i in range(len(nums)):
    		if ans.get(nums[i]) is None:
    			ans[nums[i]] = 1
    		else:
    			ans.pop(nums[i])
    	return ans.popitem()[0]