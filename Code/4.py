from typing import List

"""
寻找两个有序数组的中位数
解题思路:
法一:直接去找到中位数的位置
1、使用left、right来保存前一个和当前的值
2、使用aStart、bStart来记录两列表当前的位置
3、不管奇数个还是偶数个，迭代次数都为lens//2+1
两个判断条件
4、若nums1未达到边界，且nums2达到边界或nums2值大于1的，right为nums1当前值
5、若nums2未达到边界，且nums1达到边界或nums1值大于2的，right为nums2当前值
6、分奇偶返回
法二:二分法
结果:
1、
执行用时 :120 ms(180 ms), 在所有 python3 提交中击败了86.83%的用户
内存消耗 :14 MB, 在所有 python3 提交中击败了5.28%的用户
2、
执行用时 :120 ms, 在所有 python3 提交中击败了86.83%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.28%的用户
反思:
1、之前想的思路就是直接找中位数的位置，但并没有想清楚，主要没想到应该去保存数字，
而不是单纯的记录索引，所以很乱，没有搞清楚
2、看到时间复杂度为log，应该想到分支算法
"""

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		l1, l2 = len(nums1), len(nums2)
		lens = l1 + l2
		left, right = -1, -1
		aStart, bStart = 0, 0
		for i in range(lens//2 + 1):
			left = right
			if  aStart < l1 and (bStart >= l2 or \
				nums1[aStart] < nums2[bStart]):
				right = nums1[aStart]
				aStart += 1
			else:
				right = nums2[bStart]
				bStart += 1
		if lens % 2 == 0:
			return (left + right) / 2.0
		else:
			return right

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right :
            m1 = left +(right - left)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1 
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (c1 + c2) / 2
