from singly_linked_list import ListNode

# 单链表的转置
def reverse(l: ListNode) -> ListNode:
	l1 = l
	former = None
	while l1 != None:
		later = l1.next
		l2 = l1
		l2.next = former
		former = l2
		l1 = later
	return former