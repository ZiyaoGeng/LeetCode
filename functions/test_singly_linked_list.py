from singly_linked_list import ListNode

# 创建单链表
def create_list(nums):
	L = ListNode(0)
	l = L
	for i in nums:
		l.next = ListNode(i)
		l = l.next
	return L.next

# 输出单链表的值
def print_list_val(l):
	while l != None:
		print(l.val, end='')
		l = l.next
		if l != None:
			print('->', end='') 
	print()
