import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	p = ListNode(0)
    	p.next = head
    	head, q = p, p
    	while p.next != None and p.next.next != None:
    		if p.next.val == p.next.next.val:
    			while p.next.next != None and p.next.val == p.next.next.val:
    				p = p.next
    			q.next = p.next.next
    		else:
    			q = q.next
    		p = p.next
    	return head.next