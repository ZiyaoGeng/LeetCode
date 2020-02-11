import sys
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
    	if root == None:
    		return True
    	if abs(self.depth(root.left) - self.depth(root.right)) > 1:
    		return False
    	else:
    		return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root: TreeNode):
    	if root == None:
    		return 0
    	return 1 + max(self.depth(root.left), self.depth(root.right))
