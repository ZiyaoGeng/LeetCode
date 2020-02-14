import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    	ans = {}
    	p = headA
    	while p != None:
    		ans[p] = 1
    		p = p.next
    	q = headB
    	while q != None:
    		if ans.get(q) != None:
    			return q
    		q = q.next
    	return None