class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
    	if root == None:
    		return None
    	que = []
    	length, count = 1, 0
    	que.append(root)
    	while len(que) != 0:
    		p = que.pop(0)
    		count += 1
    		if p.left != None:
    			que.append(p.left)
    		if p.right != None:
    			que.append(p.right)
    		if count == length:
    			length = len(que)
    			count = 0
    		else:
    			p.next = que[0]
    	return root