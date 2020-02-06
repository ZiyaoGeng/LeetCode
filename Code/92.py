import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    	p, q = head, None
    	later, former = None, None
    	count = 1
    	while p != None:
    		if count == m - 1:
    			former = p
    		if count >= m:
    			r = p.next
    			p.next = q
    			q = p
    			p = r
    			if count == m:
    				later = q
    			if count == n:
    				if former != None:
    					former.next = q
    				else:
    					head = q
    				later.next = p
    				break
    		else:
    			p = p.next
    		count += 1
    	return head