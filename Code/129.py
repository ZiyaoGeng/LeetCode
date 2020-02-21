import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
    	sumload = 0
    	def helper(root, num):
    		nonlocal sumload
    		if root.left == None and root.right == None:
    			num = num * 10 + root.val
    			sumload += num
    		else:
    			num = num * 10 + root.val
    			if root.left != None:
    				helper(root.left, num)
    			if root.right != None:
    				helper(root.right, num)
    	helper(root, 0)
    	return sumload

