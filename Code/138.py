
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
    	p = head
    	ans = {}
    	former = None
    	while p != None:
    		if ans.get(p) == None:
    			clone = Node(p.val, None, None)
    			ans[p] = clone
    		else:
    			clone = ans[p]
    		if p.random == None:
    			r_node = None
    		elif ans.get(p.random) == None:
    			r_node = Node(p.random.val, None, None)
    		else:
    			r_node = ans[p.random]
    		clone.random = r_node
    		if p == head:
    			former = clone
    		else:
    			former.next = clone
    			former = former.next
    		p = p.next
    	return ans[p]