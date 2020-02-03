import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    	p, q = head, head
    	while p!= None and p.next != None:
    		p = p.next.next
    		q = q.next
    		if p == q:
    			return True
    	return False

