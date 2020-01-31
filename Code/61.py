import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
    	p, lens, c = head, 0, 0
    	while p != None:
    		lens += 1
    		p = p.next
    	if lens == 0 or k % lens == 0:
    		return head
    	k %= lens
    	p, q = head, head
    	while p.next != None:
    		if c == k:
    			q = q.next
    		else:
    			c += 1
    		p = p.next
    	r = q.next
    	p.next = head
    	q.next = None
    	return r
