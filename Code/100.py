import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	if p == None and q == None:
    		return True
    	if (p != None and q == None) or (p == None and q != None) or \
    	p.val != q.val:
    		return False
    	else:
    		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
