from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	if needle == "":
    		return 0
    	return self.KMP(haystack, needle)

    def KMP(self, A: str, B: str) -> int:
    	F = self.F(B)
    	i, j = 0, 0
    	while i < len(A):
    		if A[i] == B[j]:
    			i += 1
    			j += 1
    			if j == len(B):
    				return i - j
    		else:
    			if j == 0:
    				i += 1
    			else:
    				j = F[j-1] + 1
    	return -1

    def F(self, s: str) -> List[int]:
    	F = [-1]
    	for i in range(1, len(s)):
    		j = F[i-1]
    		while j>= 0 and s[j+1] != s[i]:
    			j = F[j]
    		if s[j+1] == s[i]:
    			F.append(j + 1)
    		else:
    			F.append(-1)
    	return F

s = Solution()
print(s.strStr("hello", "all"))
    		