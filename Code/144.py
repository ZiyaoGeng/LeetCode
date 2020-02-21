import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
    	if root == None:
    		return []
    	stack, l = [], []
    	stack.append(root)
    	while len(stack) == 0:
    		p = stack.pop(-1)
    		l.append(p.val)
    		if p.right != None:
    			stack.append(p.right)
    		if p.left != None:
    			stack.append(p.left)
    	return l

