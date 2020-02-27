import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
    	if head == None or head.next == None:
    		return head
    	low, fast = head, head.next
    	while fast!= None and fast.next != None:
    		low = low.next
    		fast = fast.next.next
    	p = low.next
    	low.next = None
    	l1 = self.sortList(head)
    	l2 = self.sortList(p)
    	l = ListNode(0)
    	q = l
    	while l1 != None and l2 != None:
    		if l1.val < l2.val:
    			q.next = l1
    			l1 = l1.next
    		else:
    			q.next = l2
    			l2 = l2.next
    		q = q.next
    	if l1 != None:
    		q.next = l1
    	if l2 != None:
    		q.next = l2
    	return l.next