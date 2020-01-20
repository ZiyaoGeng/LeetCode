from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum = nums[0]
		for i in range(1, len(nums)):
			if nums[i - 1] > 0:
				nums[i] += nums[i - 1]
			max_sum = max(max_sum, nums[i])
		return max_sum
	
    def maxSubArray(self, nums: List[int]) -> int:
    	if len(nums) == 0:
    		return 0
    	return self.func(nums, 0, len(nums)-1)

    def func(self, nums: List[int], l: int, r: int) -> int:
    	if l == r:
    		return nums[l]
    	mid = (l + r) // 2
    	ll = self.func(nums, l, mid)
    	lr = self.func(nums, mid+1, r)
    	i, j, max_l, max_r = mid, mid + 1, nums[mid], 0
    	l_val, r_val = 0, 0
    	while i >= l:
    		l_val += nums[i]
    		if l_val > max_l:
    			max_l = l_val
    		i -= 1
    	while j <= r:
    		r_val += nums[j]
    		if r_val > max_r:
    			max_r = r_val
    		j += 1
    	results = max_l + max_r
    	return max(results, ll, lr)
