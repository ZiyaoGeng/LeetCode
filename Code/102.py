import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
    	if root == None:
    		return []
    	ls, que, l = [], [], []
    	length, count = 1, 0
    	que.append(root)
    	while len(que) != 0:
    		p = que.pop(0)
    		l.append(p.val)
    		print(count)
    		if p.left != None:
    			que.append(p.left)
    		if p.right != None:
    			que.append(p.right)
    		if count == length:
    			ls.append(l.copy())
    			count = 0
    			length = len(que)
    			l = []
    	return ls