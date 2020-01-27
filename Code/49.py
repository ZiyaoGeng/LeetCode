from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	hashmap = {}
    	for s in strs:
    		ss = ''.join(sorted(s))
    		if hashmap.get(ss) is None:
    			hashmap[ss] = [s]
    		else:
    			hashmap[ss].append(s)
    	return hashmap.values()


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))