# :pencil2: Leetcode Solutions with Python
- 身份：某大学硕士研究生在读；

- 坐标：上海；

- 目的：为了一年以后的竞争，现开始系统的刷题；
- 时间：2020.1.17～

以前使用Java刷过近200题，但时间太久都遗忘了，故令开一个LeetCode号，重新开始，使用现在自己最常用的Python语言。记录每道题的题解、反思等。



### Debug：相关类或函数

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

#### 树的创建

```python
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

```

#### 如何引入

例：

```python
import sys
sys.path.append('../functions/')
from singly_linked_list import ListNode
```



### Python包：特殊的函数或用法

1. **ord()**，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值；
2. str = **str.rstrip()**，去除字符串右端的空格；
3. 遍历字典的四种方式：
   - 遍历键：`for key in hashmap:`
   - 遍历值：`for value in hashmap.values():`
   - 遍历键、值：`for key, value in hashmap:`
   - 遍历项：`for item in hashmap.items():`
4. 重复字符串只需乘以数字即可：`"a" * 2`
5. 关于2 ** 31，可以用**位运算符**，`1<<31`



### 列表

| # | Title | Type | Source Code |  Difficulty | Time | Solved |
|:---:|:---:|:---:|:---:|:---:|:---:|-----|
|1|[ 两数之和 ](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/1.md)|哈希表|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/1.py)|Easy|2020/1/17|Y|
|2|[ 两数相加 ](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/2.md)|单链表、数学|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/2.py)|Medium|2020/1/17|Y|
|3|[  无重复字符的最长子串 ](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/3.md)|滑动窗口|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/3.py)|Medium|2020/1/17|Y|
|4|[  寻找两个有序数组的中位数 ](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/submissions/)|二分查找、分治算法|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/4.py)|Hard|2019/11/4|N|
|5|[最长回文子串](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/5.md)|字符串|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/5.py)|Medium|2020/1/22|Y|
|6|[Z字形变换](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/6.md)|字符串|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/6.py)|Medium|2020/1/21|Y|
|7|[整数反转](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/7.md)|数学|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/7.py)|Easy|2020/1/17|Y|
|8|[字符串转整数(atoi)](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/8.md)|数学、字符串、**正则表达式**|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/8.py)|Medium|2020/1/22|Y|
|9|[回文数](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/9.md)|数学|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/9.py)|Easy|2020/1/17|Y|
|11|[盛最多水的容器](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/11.md)|双指针|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/11.py)|Medium|2020/1/23|Y|
|12|[整数转罗马数字](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/12.md)|字符串、哈希表|[Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/12.py)|Medium|2020/1/21|Y|
|  13  | [罗马数字转整数](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/13.md) |            哈希表            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/13.py) |    Easy    | 2020/1/17 |   Y    |
|  14  | [最长公共前缀](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/14.md) |           分治算法           | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/14.py) |    Easy    | 2020/1/18 |   Y    |
|  20  | [有效的括号](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/20.md) |          栈、哈希表          | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/20.py) |    Easy    | 2020/1/18 |   Y    |
|  21  | [合并两个有序链表](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/21.md) |         单链表、递归         | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/21.py) |    Easy    | 2020/1/18 |   Y    |
|  26  | [删除排序数组中的重复项](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/26.md) |            双指针            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/26.py) |    Easy    | 2020/1/18 |   Y    |
|  27  | [移除元素](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/27.md) |            双指针            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/27.py) |    Easy    | 2020/1/19 |   Y    |
|  28  | [实现strStr\(\)](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/28.md) |           **KMP**            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/28.py) |    Easy    | 2020/1/19 |   Y    |
|  35  | [搜索插入位置](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/26.md) |           二分查找           | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/35.py) |    Easy    | 2020/1/19 |   Y    |
|  38  | [外观数列](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/38.md) |             递归             | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/38.py) |    Easy    | 2020/1/19 |   Y    |
|  53  | [最大子序和](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/53.md) |    分治算法、**动态规划**    | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/53.py) |    Easy    | 2020/1/20 |   Y    |
|  58  | [最后一个单词的长度](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/58.md) |          **字符串**          | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/58.py) |    Easy    | 2020/1/20 |   Y    |
|  66  | [加一](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/66.md) |             逻辑             | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/66.py) |    Easy    | 2020/1/20 |   Y    |
|  67  | [二进制求和](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/66.md) |            双指针            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/67.py) |    Easy    | 2020/1/20 |   Y    |
|  69  | [x的平方根](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/69.md) |     二分查找、**牛顿法**     | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/69.py) |    Easy    | 2020/1/21 |   Y    |
|  70  | [爬楼梯](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/70.md) |      斐波那契、动态规划      | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/70.py) |    Easy    | 2020/1/20 |   Y    |
|  83  | [删除排序链表中的重复元素](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/83.md) |            单链表            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/83.py) |    Easy    | 2020/1/20 |   Y    |
|  88  | [合并两个有序数组](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/88.md) |            双指针            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/88.py) |    Easy    | 2020/1/20 |   Y    |
| 100  | [相同的树](https://github.com/BlackSpaceGZY/LeetCode/blob/master/idea/88.md) |            二叉树            | [Python](https://github.com/BlackSpaceGZY/LeetCode/blob/master/Code/100.py) |    Easy    | 2020/1/20 |   Y    |



