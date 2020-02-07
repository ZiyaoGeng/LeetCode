import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
	def __init__(self):
		self.lists = []

	def generateTrees(self, n: int) -> List[TreeNode]:
		flag = [0] * (n + 1)
		for i in range(1, n+1):
			flag[i] = 1
			self.trackback(n, TreeNode(i), [i], flag, 1)
		return self.lists

	def trackback(self, n: int, tree: TreeNode, l : List[int], flag: List[int], count: int):
		if count == n:
			self.lists.append(tree)
		else:
			for i in range(1, n+1):
				if flag[i] == 0:
					flag[i] = 1
					if tree.val < i:
						if tree.left != None:
							flag[tree.left.val] = 0
						tree.left = TreeNode(i)
						self.trackback(n, tree.left, flag, count+1)
					elif tree.val > i:
						if tree.right != None:
							flag[tree.right.val] = 0
						tree.right = TreeNode(i)
						self.trackback(n, tree.right, flag, count+1)
					
					

