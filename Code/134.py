from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    	diff = []
    	num = 0
    	for i in range(len(gas)):
    		num += gas[i] - cost[i]
    		diff.append(gas[i] - cost[i])
    	if num < 0:
    		return -1
    	num, i, length = 0, 0, 0
    	while length < len(diff):
    		if (num == 0 and diff[i] > 0) or (num + diff[i] >= 0):
    			num += diff[i]
    			length += 1
    			
    		else:
    			num = 0
    			length = 0
    		i = (i + 1) % len(diff)
    	return i
