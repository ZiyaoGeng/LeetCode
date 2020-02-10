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



t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
print(Solution().minDepth(t))