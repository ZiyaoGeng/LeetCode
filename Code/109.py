import sys
sys.path.append('../functions/')
from tree import TreeNode
from singly_linked_list import ListNode

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
    	if head == None:
    		return None
    	p = ListNode(0)
    	p.next = head
    	head = p
    	p1, p2 = head, head
    	while p2.next != None and p2.next.next != None:
    		p1 = p1.next
    		p2 = p2.next.next
    	root = TreeNode(p1.next.val)
    	q = p1.next.next
    	p1.next = None
    	root.left = self.sortedListToBST(head.next)
    	root.right = self.sortedListToBST(q)
    	return root