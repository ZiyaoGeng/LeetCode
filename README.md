# :pencil2: Leetcode Solutions with Python
- 身份：某大学硕士研究生在读；

- 坐标：上海；

- 目的：为了一年以后的竞争，现开始系统的刷题；
- 时间：2020.1.17～

以前使用Java刷过近200题，但时间太久都遗忘了，故令开一个LeetCode号，重新开始，使用现在自己最常用的Python语言。记录每道题的题解、反思等。



### 相关类或函数

因为使用Sublime作为编辑器，故没有调试功能，自己写了一些类或函数方便调用进行调试；

#### 单链表创建

```python
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
```

#### 创建单链表

```python
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
```

#### 单链表转置

```python
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
```



### 列表

| # | Title | Type | Source Code |  Difficulty | Time | Solved |
|:---:|:---:|:---:|:---:|:---:|:---:|-----|
|1|[ 两数之和 ](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/1.md)|哈希表|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/1.py)|Easy|2020/1/17|Y|
|2|[ 两数相加 ](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/2.md)|链表、数学|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/2.py)|Medium|2020/1/17|Y|
|3|[  无重复字符的最长子串 ](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/3.md)|Sliding Window|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/3.py)|Medium|2020/1/17|Y|
|4|[  寻找两个有序数组的中位数 ](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/submissions/)|二分查找、分治算法|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/4.py)|Hard|2019/11/4|N|
|7|[整数反转](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/7.md)|数学|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/7.py)|Easy|2020/1/17|Y|
|9|[回文数](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/9.md)|数学|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/9.py)|Easy|2020/1/17|Y|
|  13  | [罗马数字转整数](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/13.md) |       哈希表       | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/13.py) |    Easy    | 2020/1/17 |   Y    |
|  14  | [最长公共前缀](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/14.md) |      分治算法      | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/14.py) |    Easy    | 2020/1/18 |   Y    |



