import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List 

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    	if len(nums) == 0:
    		return None
    	mid = (len(nums) - 1) // 2
    	t = TreeNode(nums[mid])
    	self.dfs(nums, t, mid+1, len(nums)-1)
    	self.dfs(nums, t, 0, mid-1)
    	return t

    def dfs(self, nums: List[int], t: TreeNode, l: int, r: int):
    	if l <= r:
    		mid = (l + r) // 2
    		if t.val > nums[mid]:
    			t.left = TreeNode(nums[mid])
    			t = t.left
    		else:
    			t.right = TreeNode(nums[mid])
    			t = t.right
    		self.dfs(nums, t, l, mid-1)
    		self.dfs(nums, t, mid+1, r)
