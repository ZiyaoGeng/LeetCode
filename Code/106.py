import sys
sys.path.append('../functions/')
from tree import TreeNode
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    	pos_dx = len(postorder) - 1
    	idx_map = {val:idx for idx, val in enumerate(inorder)}
    	def helper(in_left=0, in_right=len(postorder)):
    		nonlocal pos_dx
    		if in_left == in_right:
    			return None
    		root = TreeNode(postorder[pos_dx])
    		index = idx_map[root.val]
    		pos_dx -= 1

    		root.right = helper(index+1, in_right)
    		root.left = helper(in_left, index)
    		
    		return root
    	return helper()
