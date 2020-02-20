import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    	if root == None:
    		return []
    	ls = []
    	def trackback(root: TreeNode, sum: int, l: List[int]):
    		if sum == 0 and root.left == None and root.right == None:
    			ls.append(l.copy())
    		else:
    			if root.left != None:
    				l.append(root.left.val)
    				trackback(root.left, sum - root.left.val, l)
    				l.pop(-1)
    			if root.right != None:
    				l.append(root.right.val)
    				trackback(root.right, sum - root.right.val, l)
    				l.pop(-1)
    	trackback(root, sum-root.val, [root.val])
    	return ls