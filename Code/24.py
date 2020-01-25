import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
    	l = ListNode(0)
    	l.next = head
    	p, q = l, l.next
    	while p.next != None and q.next != None:
    		r = q.next
    		p.next.next = q.next.next
    		s = p.next
    		r.next = s
    		p.next = r
    		p = p.next.next
    		q = q.next
    	return l.next

