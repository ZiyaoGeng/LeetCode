import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from reverse import reverse
from test_singly_linked_list import *


class Solution:

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	    flag1, flag2 = 0, 0
	    L = l1
	    L_prev = None
	    while l1 != None and l2 != None:
	    	L_prev = l1 if L_prev==None else L_prev.next
	    	flag2 = (l1.val + l2.val + flag1) // 10
	    	l1.val = (l1.val + l2.val + flag1) % 10
	    	flag1 = flag2
	    	l1 = l1.next
	    	l2 = l2.next
	    if l2 != None:
	    	l1 = l2
	    	L_prev.next = l1
	    while l1 != None:
	    	flag2 = (l1.val + flag1) // 10
	    	l1.val = (l1.val + flag1) % 10
	    	flag1 = flag2
	    	l1 = l1.next
	    	L_prev = L_prev.next
	    if flag1 == 1:
	    	L_prev.next = ListNode(1)
	    return L	    
