from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    	if len(strs) == 0:
    		return ""
    	return self.binarySearch(strs, 0, len(strs)-1)

    def binarySearch(self, strs: List[str], l: int, r: int) -> str:
    	if l == r:
    		return strs[l]
    	mid = (l + r) // 2
    	str1 = self.binarySearch(strs, l, mid)
    	str2 = self.binarySearch(strs, mid+1, r)
    	return self.findPrefix(str1, str2)

    def findPrefix(self, str1: str, str2: str) -> str:
    	lens, index = min(len(str1), len(str2)), 0
    	strs = ""
    	for i in range(lens):
    		if str1[i] == str2[i]:
    			index += 1
    		else:
    			break
    	strs += str1[:index]
    	return strs