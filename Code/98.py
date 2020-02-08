import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
	def __init__(self):
		self.flag = True

	def isValidBST(self, root: TreeNode) -> bool:
		if root == None:
			return True
		self.dfs(root, None, None)
		return self.flag
    	
	def dfs(self, p: TreeNode, q: TreeNode, r: TreeNode):
		if self.flag == False:
			return
		s = r
		if p.left != None:
			if q!= None and q.right == p:
					r = q
			if p.left.val >= p.val or (r != None and p.left.val <= r.val):
				self.flag = False
			else:
				self.dfs(p.left, p, r)
		r = s
		if p.right != None:
			if q!= None and q.left == p:
					r = q
			if p.right.val <= p.val or (r!= None and p.right.val >= r.val):
				self.flag = False
			else:
				self.dfs(p.right, p, r)