from typing import List

"""
两数之和
解题思路:
1、两遍循环；
2、一遍循环，调用list的index函数，去寻找对应值是否存在（其实和1差不多）
3、采用hashmap（没想到，好久没用哈希了），并且主要没发现输出两个索引的顺序是不
重要的。
结果:
2、
执行用时 :900 ms, 在所有 python3 提交中击败了35.57%的用户
内存消耗 :14.7 MB, 在所有 python3 提交中击败了6.86%的用户
3、
执行用时 :60 ms, 在所有 python3 提交中击败了97.18%的用户
内存消耗 :15 MB, 在所有 python3 提交中击败了5.05%的用户
反思:
哈希表的应用最为关键！！！
"""

class Solution:
	# 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	j = 0
    	for i in range(len(nums)):
    		num = target - nums[i]
    		if num in nums[i+1:]:
    			j = nums[i+1:].index(num) + i + 1
    			break
    	return [i, j]

    # 3
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	hashmap = {}
    	for i, num in enumerate(nums):
    		if hashmap.get(target - num) is not None:
    			return [i, hashmap.get(target - num)]
    		hashmap[num] = i
