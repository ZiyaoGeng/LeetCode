from typing import List

class Solution:
	# 2
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		if len(intervals) == 0:
			return []
		new = []
		intervals = sorted(intervals, key=lambda x:x[0])
		l, r = intervals[0][0], intervals[0][1]
		for it in intervals[1:]:
			if r >= it[0] and r < it[1]:
				r = it[1]
			elif r < it[0]:
				new.append([l, r])
				l = it[0]
				r = it[1]
		new.append([l, r])
		return new

	# 1	
	"""
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals = sorted(intervals, key=lambda x:x[1])
		i = len(intervals) - 1
		while i > 0:
			if intervals[i][0] <= intervals[i-1][1]:
				intervals[i][0] = intervals[i][0] if \
				intervals[i][0] <= intervals[i-1][0] else intervals[i-1][0]
				intervals.remove(intervals[i-1])
			i -= 1
		return intervals
	"""
