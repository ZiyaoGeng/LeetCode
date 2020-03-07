
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
    	v1 = version1.split('.')
    	v2 = version2.split('.')
    	l1, l2 = 0, 0
    	while l1 < len(v1) and l2 < len(v2):
    		if int(v1[l1]) > int(v2[l2]):
    			return 1
    		elif int(v1[l1]) < int(v2[l2]):
    			return -1
    		l1 += 1
    		l2 += 1
    	while l1 < len(v1):
    		if int(v1[l1]) > 0:
    			return 1
    		l1 += 1
    	while l2 < len(v2):
    		if int(v2[l2]) > 0:
    			return -1
    		l2 += 1
    	return 0 

print(Solution().compareVersion("1.0.0", "0"))
