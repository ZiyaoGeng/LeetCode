import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
	def __init__(self):
		self.flag = False
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		if root == None:
			return False
		self.dfs(root, sum - root.val)
		return self.flag
	def dfs(self, root: TreeNode, sum: int):
		if root.left == None and root.right == None:
			if sum == 0::
				self.flag = True
		else:
			if root.left != None:
				self.dfs(root.left, sum - root.left.val)
			if root.right != None:
				self.dfs(root.right, sum - root.right.val)