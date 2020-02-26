import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
    	if head == None:
    		return None
    	p = ListNode(0)
    	p.next = head
    	head = p
    	sort, p = head, head.next
    	while p.next != None:
    		if p.val < p.next.val:
    			p = p.next
    			continue
    		r = sort
    		while p.next.val > r.next.val:
    			r = r.next
    		if r.next != p.next:
    			q = p.next
    			p.next = p.next.next
    			q.next = r.next
    			r.next = q
    	return sort.next