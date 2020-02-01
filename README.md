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
6. 排序，`sorted(nums, key= lambda x: x[1])`，按照每一个迭代对象的第2个值进行排序
7. 创建二维数组：`[[0] * n for i in range(n)]`



### 列表

| # | Title | Type | Source Code |  Difficulty | Time | Solved |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1|[ 两数之和 ](./idea/1.md)|哈希表|[Python](./Code/1.py)|Easy|2020/1/17|Y|
|2|[ 两数相加 ](./idea/2.md)|单链表、数学|[Python](./Code/2.py)|Medium|2020/1/17|Y|
|3|[  无重复字符的最长子串 ](./idea/3.md)|滑动窗口|[Python](./Code/3.py)|Medium|2020/1/17|Y|
|4|[  寻找两个有序数组的中位数 ](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/submissions/)|二分查找、分治算法|[Python](./Code/4.py)|Hard|2019/11/4|N|
|5|[最长回文子串](./idea/5.md)|字符串|[Python](./Code/5.py)|Medium|2020/1/22|Y|
|6|[Z字形变换](./idea/6.md)|字符串|[Python](./Code/6.py)|Medium|2020/1/21|Y|
|7|[整数反转](./idea/7.md)|数学|[Python](./Code/7.py)|Easy|2020/1/17|Y|
|8|[字符串转整数(atoi)](./idea/8.md)|数学、字符串、**正则表达式**|[Python](./Code/8.py)|Medium|2020/1/22|Y|
|9|[回文数](./idea/9.md)|数学|[Python](./Code/9.py)|Easy|2020/1/17|Y|
|11|[盛最多水的容器](./idea/11.md)|双指针|[Python](./Code/11.py)|Medium|2020/1/23|Y|
|12|[整数转罗马数字](./idea/12.md)|字符串、哈希表|[Python](./Code/12.py)|Medium|2020/1/21|Y|
|  13  |                [罗马数字转整数](./idea/13.md)                |            哈希表            | [Python](./Code/13.py)  |    Easy    | 2020/1/17 |   Y    |
|  14  |                 [最长公共前缀](./idea/14.md)                 |           分治算法           | [Python](./Code/14.py)  |    Easy    | 2020/1/18 |   Y    |
|  15  |                   [三数之和](./idea/15.md)                   |         数组、双指针         | [Python](./Code/15.py)  |   Medium   | 2020/1/24 |   N    |
|  16  |               [最接近的三数之和](./idea/16.md)               |         数组、双指针         | [Python](./Code/16.py)  |   Medium   | 2020/1/25 |   Y    |
|  17  |              [电话号码的字母组合](./idea/17.md)              |         字符串、回溯算法         | [Python](./Code/17.py)  |   Medium   | 2020/1/23 |   Y    |
|  18  |                   [四数之和](./idea/18.md)                   |         数组、双指针         | [Python](./Code/18.py)  |   Medium   | 2020/1/25 |   Y    |
|  19  |           [删除链表的倒数第N个节点](./idea/19.md)            |            单链表            | [Python](./Code/19.py)  |   Medium   | 2020/1/23 |   Y    |
|  20  |                  [有效的括号](./idea/20.md)                  |          栈、哈希表          | [Python](./Code/20.py)  |    Easy    | 2020/1/18 |   Y    |
|  21  |               [合并两个有序链表](./idea/21.md)               |         单链表、递归         | [Python](./Code/21.py)  |    Easy    | 2020/1/18 |   Y    |
|  22  |                   [括号生成](./idea/22.md)                   |         字符串、回溯算法         | [Python](./Code/22.py)  |   Medium   | 2020/1/25 |   Y    |
|  24  |             [两两交换链表中的节点](./idea/24.md)             |            单链表            | [Python](./Code/24.py)  |   Medium   | 2020/1/25 |   Y    |
|  26  |            [删除排序数组中的重复项](./idea/26.md)            |            双指针            | [Python](./Code/26.py)  |    Easy    | 2020/1/18 |   Y    |
|  27  |                   [移除元素](./idea/27.md)                   |            双指针            | [Python](./Code/27.py)  |    Easy    | 2020/1/19 |   Y    |
|  28  |                [实现strStr\(\)](./idea/28.md)                |           **KMP**            | [Python](./Code/28.py)  |    Easy    | 2020/1/19 |   Y    |
| 29 | [两数相除](./idea/29.md) | 数学、移位运算 | [Python](./Code/29.py) | Medium | 2020/1/26 | Y |
| 31 | [下一个排列](./idea/31.md) | 数组 | [Python](./Code/31.py) | Medium | 2020/1/29 | **N** |
| 33 | [搜索旋转排序数组](./idea/33.md) | 二分查找 | [Python](./Code/33.py) | Medium | 2020/1/26 | Y |
| 34 | [在排序数组中查找元素的第一个和最后一个位置](./idea/34.md) | 二分查找 | [Python](./Code/34.py) | Medium | 2020/1/26 | Y |
|  35  |                 [搜索插入位置](./idea/35.md)                 |           二分查找           | [Python](./Code/35.py)  |    Easy    | 2020/1/19 |   Y    |
| 36 | [有效的数独](./idea/36.md) | 哈希表 | [Python](./Code/36.py) | Medium | 2020/1/29 | Y |
|  38  |                   [外观数列](./idea/38.md)                   |             递归             | [Python](./Code/38.py)  |    Easy    | 2020/1/19 |   Y    |
| 39 | [组合总和](./idea/39.md) | 回溯算法 | [Python](./Code/39.py) | Medium | 2020/1/28 | Y |
| 40 | [组合总和II](./idea/40.md) | 回溯算法、**剪枝** | [Python](./Code/40.py) | Medium | 2020/1/28 | Y |
| 43 | [字符串相乘](./idea/43.md) | 字符串 | [Python](./Code/43.py) | Medium | 2020/1/27 | Y |
| 46 | [全排列](./idea/46.md) | DFS | [Python](./Code/46.py) | Medium | 2020/1/29 | Y |
| 47 | [全排列II](./idea/47.md) | 回溯算法、剪枝 | [Python](./Code/47.py) | Medium | 2020/1/29 | Y |
| 48 | [旋转图像](./idea/48.md) | 数组 | [Python](./Code/48.py) | Medium | 2020/1/28 | Y |
| 49 | [字母异位词分组](./idea/49.md) | 哈希表 | [Python](./Code/49.py) | Medium | 2020/1/27 | Y |
| 50 | [Pow(x, n)](./idea/50.md) | 数学 | [Python](./Code/50.py) | Medium | 2020/1/28 | Y |
|  53  |                  [最大子序和](./idea/53.md)                  |    分治算法、**动态规划**    | [Python](./Code/53.py)  |    Easy    | 2020/1/20 |   Y    |
| 54 | [螺旋矩阵](./idea/54.md) | 数组 | [Python](./Code/54.py) | Medium | 2020/1/30 | Y |
| 55 | [跳跃游戏](./idea/55.md) | **贪心算法** | [Python](./Code/55.py) | Medium | 2020/1/30 | Y |
| 56 | [合并区间](./idea/56.md) | 数组、排序 | [Python](./Code/56.py) | Medium | 2020/1/30 | Y |
|  58  |              [最后一个单词的长度](./idea/58.md)              |          **字符串**          | [Python](./Code/58.py)  |    Easy    | 2020/1/20 |   Y    |
| 59 | [螺旋矩阵II](./idea/59.md) | 数组 | [Python](./Code/59.py) | Medium | 2020/1/31 | Y |
| 60 | [第k个排列](./idea/60.md) | **数学** | [Python](./Code/60.py) | Medium | 2020/1/31 | Y |
| 61 | [旋转链表](./idea/61.md) | 单链表 | [Python](./Code/61.py) | Medium | 2020/1/31 | Y |
| 62 | [不同路径](./idea/62.md) | **动态规划** | [Python](./Code/62.py) | Medium | 2020/2/1 | Y |
| 63 | [不同路径II](./idea/63.md) | 动态规划 | [Python](./Code/63.py) | Medium | 2020/2/1 | Y |
| 64 | [最小路径和](./idea/64.md) | 动态规划 | [Python](./Code/64.py) | Medium | 2020/2/1 | Y |
|  66  |                     [加一](./idea/66.md)                     |             逻辑             | [Python](./Code/66.py)  |    Easy    | 2020/1/20 |   Y    |
|  67  |                  [二进制求和](./idea/66.md)                  |            双指针            | [Python](./Code/67.py)  |    Easy    | 2020/1/20 |   Y    |
|  69  |                  [x的平方根](./idea/69.md)                   |     二分查找、**牛顿法**     | [Python](./Code/69.py)  |    Easy    | 2020/1/21 |   Y    |
|  70  |                    [爬楼梯](./idea/70.md)                    |      斐波那契、动态规划      | [Python](./Code/70.py)  |    Easy    | 2020/1/20 |   Y    |
|  83  |           [删除排序链表中的重复元素](./idea/83.md)           |            单链表            | [Python](./Code/83.py)  |    Easy    | 2020/1/20 |   Y    |
|  88  |               [合并两个有序数组](./idea/88.md)               |            双指针            | [Python](./Code/88.py)  |    Easy    | 2020/1/20 |   Y    |
| 100  |                   [相同的树](./idea/88.md)                   |            二叉树            | [Python](./Code/100.py) |    Easy    | 2020/1/20 |   Y    |



