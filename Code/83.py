import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
from test_singly_linked_list import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	l = head 
    	while l != None and l.next != None:
    		if l.next.val == l.val:
    			l.next = l.next.next
    		else:
    			l = l.next
    	return head

s = Solution()
l = create_list([])
print_list_val(s.deleteDuplicates(l))