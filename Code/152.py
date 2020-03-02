from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	minP = [0] * len(nums)
    	maxP = [0] * len(nums)
    	for i in range(len(nums)-1, -1, -1):
    		if i == len(nums) - 1:
    			minP[i] = nums[i]
    			maxP[i] = nums[i]
    		else:
    			num1 = nums[i] * minP[i+1]
    			num2 = nums[i] * maxP[i+1]
    			maxP[i] = max(num1, num2, nums[i], maxP[i+1])
    			minP[i] = min(num1, nums[i], minP[i+1])
    	return maxP[i]

print(Solution().maxProduct([2,3,-2,4]))
