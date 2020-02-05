import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
    	p = ListNode(0)
    	p.next = head
    	head = p
    	flag = False
    	while p.next != None:
    		if p.next.val >= x and flag == False:
    			q = p 
    			flag = True
    			p = p.next
    		elif p.next.val < x and flag == True:
    			r = p.next
    			p.next = p.next.next
    			r.next = q.next
    			q.next = r 
    			q = q.next
    		else:
    			p = p.next
    	return head.next