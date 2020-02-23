import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    	if head == None:
    		return None
    	ans = {}
    	p, q = head, head.next
    	while q != None:
    		ans[p] = 1
    		if ans.get(q) != None:
    			return q
    		p = p.next
    		q = q.next
    	return None