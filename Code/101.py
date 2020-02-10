import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	if root == None:
    		return True
    	return self.dfs(root.left, root.right)

    def dfs(self, l: TreeNode, r: TreeNode):
    	if l == None and r == None:
    		return True
    	if (l != None and r == None) or (l == None and \
    		r != None) or (l.val != r.val):
    		return False
    	else:
    		return self.dfs(l.left, r.right) and self.dfs(l.right, r.left)

    def isSymmetric(self, root: TreeNode) -> bool:
    	if root == None:
    		return True
    	stack = []
    	p, q = root.left, root.right
    	while len(stack) > 0 or p != None or q != None:
    		while p != None and q != None:
    			stack.append(p)
    			stack.append(q)
    			p = p.left
    			q = q.right
    		if (p == None and q != None) or (p != None and q == None):
    			return False
    		if len(stack) > 1:
    			q = stack.pop(-1)
    			p = stack.pop(-1)
    			if p.val != q.val:
    				return False
    			p = p.right
    			q = q.left
    	return True