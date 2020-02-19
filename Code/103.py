import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    	if root == None:
    		return []
    	ls, que, l, child = [], [], [], []
    	flag = 0
    	que.append(root)
    	while len(que) != 0:
    		p = que.pop(-1)
    		if flag == 0:
    			if p.left != None:
    				child.append(p.left)
    			if p.right != None:
    				child.append(p.right)
    		else:
    			if p.right != None:
    				child.append(p.right)
    			if p.left != None:
    				child.append(p.left)
    		l.append(p.val)
    		if len(que) == 0:
    			ls.append(l.copy())
    			que = child.copy()
    			l, child = [], []
    			flag = 0 if flag == 1 else 1
    	return ls





