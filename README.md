# :pencil2: Leetcode Solutions with Python
- 身份：某大学硕士研究生在读；

- 坐标：上海；

- 目的：为了一年以后的竞争，现开始系统的刷题；
- 时间：2020.1.17～

以前使用Java刷过近200题，但时间太久都遗忘了，故令开一个LeetCode号，重新开始，使用现在自己最常用的Python语言。记录每道题的题解、反思等。



### 阶段性总结

**1～100题：**

- 未作出的Medium：15、31、95、96；【双指针】【数组】【线索二叉树】
- 重新回顾：28、40、53、55、58、60、62、79、81、89、94、98；
- Hard题等刷到200题之后再回过来做；



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

1. **ord()**，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值；**chr()**：ASCII转字符

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

8. 向后遍历：`for i in range(len(nums)-1,-1,-1)`

9. 字符串判断：

   - 是否为数字：`"".isdigit`;
   - 是否为字母：`"".isalpha`;
   - 是否为数字字母：`"".isalnum`;

   



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
|  **28**  |                [实现strStr\(\)](./idea/28.md)                |           **KMP**            | [Python](./Code/28.py)  |    Easy    | 2020/1/19 |   Y    |
| 29 | [两数相除](./idea/29.md) | 数学、移位运算 | [Python](./Code/29.py) | Medium | 2020/1/26 | Y |
| 31 | [下一个排列](./idea/31.md) | 数组 | [Python](./Code/31.py) | Medium | 2020/1/29 | **N** |
| 33 | [搜索旋转排序数组](./idea/33.md) | 二分查找 | [Python](./Code/33.py) | Medium | 2020/1/26 | Y |
| 34 | [在排序数组中查找元素的第一个和最后一个位置](./idea/34.md) | 二分查找 | [Python](./Code/34.py) | Medium | 2020/1/26 | Y |
|  35  |                 [搜索插入位置](./idea/35.md)                 |           二分查找           | [Python](./Code/35.py)  |    Easy    | 2020/1/19 |   Y    |
| 36 | [有效的数独](./idea/36.md) | 哈希表 | [Python](./Code/36.py) | Medium | 2020/1/29 | Y |
|  38  |                   [外观数列](./idea/38.md)                   |             递归             | [Python](./Code/38.py)  |    Easy    | 2020/1/19 |   Y    |
| 39 | [组合总和](./idea/39.md) | 回溯算法 | [Python](./Code/39.py) | Medium | 2020/1/28 | Y |
| **40** | [组合总和II](./idea/40.md) | 回溯算法、**剪枝** | [Python](./Code/40.py) | Medium | 2020/1/28 | Y |
| 43 | [字符串相乘](./idea/43.md) | 字符串 | [Python](./Code/43.py) | Medium | 2020/1/27 | Y |
| 46 | [全排列](./idea/46.md) | DFS | [Python](./Code/46.py) | Medium | 2020/1/29 | Y |
| 47 | [全排列II](./idea/47.md) | 回溯算法、剪枝 | [Python](./Code/47.py) | Medium | 2020/1/29 | Y |
| 48 | [旋转图像](./idea/48.md) | 数组 | [Python](./Code/48.py) | Medium | 2020/1/28 | Y |
| 49 | [字母异位词分组](./idea/49.md) | 哈希表 | [Python](./Code/49.py) | Medium | 2020/1/27 | Y |
| 50 | [Pow(x, n)](./idea/50.md) | 数学 | [Python](./Code/50.py) | Medium | 2020/1/28 | Y |
|  **53**  |                  [最大子序和](./idea/53.md)                  |    分治算法、**动态规划**    | [Python](./Code/53.py)  |    Easy    | 2020/1/20 |   Y    |
| 54 | [螺旋矩阵](./idea/54.md) | 数组 | [Python](./Code/54.py) | Medium | 2020/1/30 | Y |
| **55** | [跳跃游戏](./idea/55.md) | **贪心算法** | [Python](./Code/55.py) | Medium | 2020/1/30 | Y |
| 56 | [合并区间](./idea/56.md) | 数组、排序 | [Python](./Code/56.py) | Medium | 2020/1/30 | Y |
|  **58**  |              [最后一个单词的长度](./idea/58.md)              |          **字符串**          | [Python](./Code/58.py)  |    Easy    | 2020/1/20 |   Y    |
| 59 | [螺旋矩阵II](./idea/59.md) | 数组 | [Python](./Code/59.py) | Medium | 2020/1/31 | Y |
| **60** | [第k个排列](./idea/60.md) | **数学** | [Python](./Code/60.py) | Medium | 2020/1/31 | Y |
| 61 | [旋转链表](./idea/61.md) | 单链表 | [Python](./Code/61.py) | Medium | 2020/1/31 | Y |
| **62** | [不同路径](./idea/62.md) | **动态规划** | [Python](./Code/62.py) | Medium | 2020/2/1 | Y |
| 63 | [不同路径II](./idea/63.md) | 动态规划 | [Python](./Code/63.py) | Medium | 2020/2/1 | Y |
| 64 | [最小路径和](./idea/64.md) | 动态规划 | [Python](./Code/64.py) | Medium | 2020/2/1 | Y |
|  66  |                     [加一](./idea/66.md)                     |             逻辑             | [Python](./Code/66.py)  |    Easy    | 2020/1/20 |   Y    |
|  67  |                  [二进制求和](./idea/66.md)                  |            双指针            | [Python](./Code/67.py)  |    Easy    | 2020/1/20 |   Y    |
|  69  |                  [x的平方根](./idea/69.md)                   |     二分查找、**牛顿法**     | [Python](./Code/69.py)  |    Easy    | 2020/1/21 |   Y    |
|  70  |                    [爬楼梯](./idea/70.md)                    |      斐波那契、动态规划      | [Python](./Code/70.py)  |    Easy    | 2020/1/20 |   Y    |
| 71 | [简化路径](./idea/71.md) | 字符串、栈 | [Python](./Code/71.py) | Medium | 2020/2/9 | Y |
| 73 | [矩阵置零](./idea/73.md) | **数组** | [Python](./Code/73.py) | Medium | 2020/2/2 | Y |
| 74 | [搜索二维矩阵](./idea/74.md) | 数组、二分查找 | [Python](./Code/74.py) | Medium | 2020/2/2 | Y |
| 75 | [搜索二维矩阵](./idea/75.md) | 数组 | [Python](./Code/75.py) | Medium | 2020/2/2 | Y |
| 77 | [组合](./idea/77.md) | 回溯算法 | [Python](./Code/77.py) | Medium | 2020/2/3 | Y |
| 78 | [子集](./idea/78.md) | 回溯算法 | [Python](./Code/78.py) | Medium | 2020/2/3 | Y |
| **79** | [单词搜索](./idea/79.md) | **回溯算法** | [Python](./Code/79.py) | Medium | 2020/2/3 | Y |
| 80 | [删除排序数组中的重复项II](./idea/80.md) | 数组 | [Python](./Code/80.py) | Medium | 2020/2/4 | Y |
| **81** | [搜索旋转排序数组II](./idea/81.md) | **二分查找** | [Python](./Code/81.py) | Medium | 2020/2/4 | Y |
| 82 | [删除排序链表中的重复元素II](./idea/82.md) | 单链表 | [Python](./Code/82.py) | Medium | 2020/2/4 | Y |
|  83  |           [删除排序链表中的重复元素](./idea/83.md)           |            单链表            | [Python](./Code/83.py)  |    Easy    | 2020/1/20 |   Y    |
| 86 | [分隔链表](./idea/86.md) | 单链表 | [Python](./Code/86.py) | Medium | 2020/2/5 | Y |
|  88  |               [合并两个有序数组](./idea/88.md)               |            双指针            | [Python](./Code/88.py)  |    Easy    | 2020/1/20 |   Y    |
| **89** | [格雷编码](./idea/89.md) | **回溯算法** | [Python](./Code/89.py) | Medium | 2020/2/5 | **Y** |
| 90 | [子集II](./idea/90.md) | 回溯算法 | [Python](./Code/90.py) | Medium | 2020/2/5 | Y |
| 91 | [解码方法](./idea/91.md) | 字符串、动态规划 | [Python](./Code/91.py) | Medium | 2020/2/6 | Y |
| 92 | [反转链表II](./idea/92.md) | 单链表 | [Python](./Code/92.py) | Medium | 2020/2/6 | Y |
| 93 | [复原IP地址](./idea/93.md) | 回溯算法 | [Python](./Code/93.py) | Medium | 2020/2/6 | Y |
| **94** | [二叉树的中序遍历](./idea/94.md) | 二叉树 | [Python](./Code/94.py) | Medium | 2020/2/7 | Y |
| **95** | [不同的线索二叉树II](./idea/95.md) | 二叉搜索树 | [Python](./Code/95.py) | Medium | 2020/2/9 | N |
| **96** | [不同的线索二叉树](./idea/96.md) | 动态规划、二叉搜索树 | [Python](./Code/96.py) | Medium | 2020/2/7 | N |
| **98** | [验证二叉线索树](./idea/98.md) | DFS、二叉搜索树 | [Python](./Code/98.py) | Medium | 2020/2/8 | Y |
| 100  |                   [相同的树](./idea/100.md)                   |            二叉树            | [Python](./Code/100.py) |    Easy    | 2020/1/20 |   Y    |
| 101 | [对称二叉树](./idea/101.md) | 二叉树、DFS、栈 | [Python](./Code/101.py) | Easy | 2020/2/10 | Y |
| 102 | [二叉树的层次遍历](./idea/102.md) | 二叉树、BFS | [Python](./Code/102.py) | Medium | 2020/2/18 | Y |
| 103 | [二叉树的锯齿形层次遍历](./idea/103.md) | 二叉树、BFS | [Python](./Code/103.py) | Medium | 2020/2/18 | Y |
| 104 | [二叉树的最大深度](./idea/104.md) | 二叉树、DFS | [Python](./Code/104.py) | Easy | 2020/2/10 | Y |
| 105 | [从前序与中序遍历序列构造二叉树](./idea/105.md) | 二叉树、DFS | [Python](./Code/105.py) | Medium | 2020/2/19 | Y |
| 107 | [二叉树的层次遍历II](./idea/107.md) | 二叉树、BFS | [Python](./Code/107.py) | Easy | 2020/2/10 | Y |
| 108 | [将有序数组转化为二叉搜索树](./idea/108.md) | 二叉搜索树、DFS | [Python](./Code/108.py) | Easy | 2020/2/11 | Y |
| 110 | [平衡二叉树](./idea/110.md) | 平衡二叉树、DFS | [Python](./Code/110.py) | Easy | 2020/2/11 | Y |
| **111** | [二叉树的最小深度](./idea/111.md) | 二叉树、BFS、DFS | [Python](./Code/111.py) | Easy | 2020/2/10 | Y |
| 112 | [路径总和](./idea/110.md) | 二叉树、DFS | [Python](./Code/112.py) | Easy | 2020/2/12 | Y |
| 118 | [杨辉三角](./idea/118.md) | 数组 | [Python](./Code/118.py) | Easy | 2020/2/12 | Y |
| 119 | [杨辉三角II](./idea/119.md) | 数组 | [Python](./Code/119.py) | Easy | 2020/2/12 | Y |
| 121 | [买卖股票的最佳时机](./idea/121.md) | 动态规划 | [Python](./Code/121.py) | Easy | 2020/2/13 | Y |
| 122 | [买卖股票的最佳时机II](./idea/122.md) | 动态规划 | [Python](./Code/122.py) | Easy | 2020/2/13 | Y |
| 125 | [验证回文串](./idea/125.md) | 字符串 | [Python](./Code/125.py) | Easy | 2020/2/13 | Y |
| 136 | [只出现一次的数字](./idea/136.md) | 哈希表、**位操作** | [Python](./Code/136.py) | Easy | 2020/2/13 | Y |
| 141 | [环形链表](./idea/141.md) | 单链表 | [Python](./Code/141.py) | Easy | 2020/2/4 | Y |
| 155 | [最小栈](./idea/155.md) | 栈、设计 | [Python](./Code/155.py) | Easy | 2020/2/14 | Y |
| **160** | [相交链表](./idea/160.md) | 单链表、哈希表、**双指针** | [Python](./Code/160.py) | Easy | 2020/2/14 | Y |
| 167 | [两数之和 II - 输入有序数组](./idea/167.md) | 数组、哈希表、双指针 | [Python](./Code/167.py) | Easy | 2020/2/14 | Y |
| 168 | [Excel表列名称](./idea/168.md) | 数学 | [Python](./Code/168.py) | Easy | 2020/2/15 | Y |
| **169** | [多数元素](./idea/169.md) | 分治、投票 | [Python](./Code/169.py) | Easy | 2020/2/15 | Y |
| 171 | [Excel表列序号](./idea/171.md) | 数学 | [Python](./Code/171.py) | Easy | 2020/2/16 | Y |
| **172** | [阶乘后的零](./idea/172.md) | 数学 | [Python](./Code/172.py) | Easy | 2020/2/17 | Y |
| 189 | [旋转数组](./idea/189.md) | 数组 | [Python](./Code/189.py) | Easy | 2020/2/17 | Y |
| 190 | [颠倒二进制位](./idea/190.md) | 位运算 | [Python](./Code/190.py) | Easy | 2020/2/17 | Y |
| 191 | [位1的个数](./idea/191.md) | 位运算 | [Python](./Code/191.py) | Easy | 2020/2/17 | Y |
| 198 | [打家劫舍](./idea/198.md) | 动态规划 | [Python](./Code/198.py) | Easy | 2020/2/17 | Y |



