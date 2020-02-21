import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
    	if root == None:
    		return
    	stack = []
    	stack.append(root)
    	q = root
    	while len(stack) != 0:
    		p = stack.pop(-1)
    		if p.right != None:
    			stack.append(p.right)
    		if p.left != None:
    			stack.append(p.left)
    		if p != root:
    			q.right = p
    			q.left = None
    			q = q.right

