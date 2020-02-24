import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def reorderList(self, head: ListNode) -> None:
    	if head == None:
    		return 
    	p, q = head, head.next
    	while q != None and q.next != None:
    		p = p.next
    		q = q.next.next
    	latter = p.next
    	p.next = None
    	def reverse(head):
    		former = None
    		p = head
    		while p != None:
    			latter = p.next
    			p.next = former
    			former = p
    			p = latter
    		return former

    	reverse_latter = reverse(latter)
    	p = head
    	while reverse_latter != None:
    		q = p.next
    		r = reverse_latter.next
    		p.next = reverse_latter
    		reverse_latter.next = q
    		p = p.next.next
    		reverse_latter = r