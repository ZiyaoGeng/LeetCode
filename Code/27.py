from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	if len(nums) == 0:
    		return 0
    	else:
    		index = 0
    		for i in range(len(nums)):
    			if nums[i] != val:
    				nums[index] = nums[i]
    				index += 1
    		return index 


s = Solution()
print(s.removeElement([], 9))
