from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    	wordDict = dict(zip(wordDict, [0]*len(wordDict)))
    	dp = [False] * (len(s) + 1)
    	dp[-1] = True
    	for i in range(len(s)-1, -1, -1):
    		for j in range(i, len(s)):
    			if wordDict.get(s[i:j+1]) != None and dp[j+1]:
    				dp[i] = True
    				break
    	return dp[0]