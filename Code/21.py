import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    	l = ListNode(0)
    	p, q, r = l1, l2, l
    	while p != None and q != None:
    		if p.val < q.val:
    			r.next = p
    			p = p.next
    		else:
    			r.next = q
    			q = q.next
    		r = r.next
    	if q != None:
    		p = q
    	r.next = p
    	return l.next

s = Solution()
l1 = create_list([])
l2 = create_list([1, 3, 4])
l = s.mergeTwoLists(l1, l2)
print_list_val(l)