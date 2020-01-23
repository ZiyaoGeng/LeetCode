import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    	count = 0
    	pre, q = head, head
    	while q.next != None:
    		q = q.next
    		if count == n:
    			pre = pre.next
    		if count != n:
    			count += 1
    	if count != n:
    		return head.next
    	pre.next = pre.next.next
    	return head
