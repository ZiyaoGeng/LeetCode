import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def minDepth(self, root: TreeNode) -> int:
    	if root == None:
    		return 0
    	que = []
    	que.append(root)
    	depth, lens, count = 1, 1, 0
    	while len(que) > 0:
    		p = que.pop(0)
    		count += 1
    		if p.left != None:
    			que.append(p.left)
    		if p.right != None:
    			que.append(p.right)
    		if p.left == None and p.right == None:
    			return depth
    		if count == lens:
    			count = 0
    			lens = len(que)
    			depth += 1

    def minDepth2(self, root: TreeNode) -> int:
    	if root == None:
    		return 0
    	return self.dfs(root, 1)

    def dfs(self, p: TreeNode, l: int):
    	if p.left == None and p.right == None:
    		return l
    	l1, l2 = float('inf'), float('inf')
    	if p.left != None:
    		l1 = self.dfs(p.left, l+1)
    	if p.right != None:
    		l2 = self.dfs(p.right, l+1)
    	return min(l1, l2)