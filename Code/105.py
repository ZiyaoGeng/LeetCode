import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	i = 0
    	while i < len(inorder) and preorder[0] != inorder[i]:
    		i += 1
    	if i < len(inorder):
    		p = TreeNode(inorder[i])
    		p.left = self.buildTree(preorder[1:i+1], inorder[:i-1])
    		p.right = self.buildTree(preorder[i+1:], inorder[i+1:])
    		return p
    	return None

