import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    	l, stack = [], []
    	p = root
    	while len(stack) > 0 or p != None:
    		while p != None:
    			stack.append(p)
    			p = p.left
    		if len(stack) > 0:
    			p = stack.pop()
    			l.append(p.val)
    			p = p.right
    	return l