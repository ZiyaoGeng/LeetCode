from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    	nums = sorted(nums)
    	i, j = 0, len(nums) - 1
    	lists = []
    	while i < j:
    		if nums[i] + nums[j] <= 0:
    			k = j - 1
    			while k > i and nums[k] >= 0:
    				if nums[i] + nums[j] + nums[k] == 0:
    					lists.append([nums[i], nums[k], nums[j]])
    					break
    				k -= 1
    			i += 1
    			while i < j and nums[i] == nums[i - 1]:
    				i += 1
    		else:
    			k = i + 1
    			while k < j and nums[k] < 0:
    				if nums[i] + nums[j] + nums[k] == 0:
    					lists.append([nums[i], nums[k], nums[j]])
    					break
    				k += 1
    			j -= 1
    			while i < j and nums[j] == nums[j + 1]:
    				j -= 1
    	return lists


s = Solution()
print(s.threeSum([-2,0,1,1,2]))