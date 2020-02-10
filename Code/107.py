import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    	if root == None:
    		return None
    	ls, l, queue = [], [], []
    	queue.append(root)
    	lens, count = 1, 0
    	while len(queue) > 0:
    		p = queue.pop(0)
    		l.append(p.val)
    		count += 1
    		if p.left != None:
    			queue.append(p.left)
    		if p.right != None:
    			queue.append(p.right)
    		if lens == count:
    			ls.insert(0, l.copy())
    			l = []
    			count = 0
    			lens = len(queue)
    	return ls

