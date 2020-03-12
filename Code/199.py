from typing import List
import sys
sys.path.append('../functions/')
from tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
    	if root == None:
    		return None
    	que, l = [], []
    	count, length = 0, 1
    	que.append(root)
    	while len(que) != 0:
    		p = que.pop(0)
    		count += 1
    		if p.left != None:
    			que.append(p.left)
    		if p.right != None:
    			que.append(p.right)
    		if count == length:
    			l.append(p.val)
    			length = len(que)
    			count = 0
    	return l

