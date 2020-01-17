

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	flag, memory = [-1] * 128, []
    	max_len, lens = 0, 0
    	for i in range(len(s)):
    		if flag[ord(s[i])] == -1:
    			memory.append(ord(s[i]))
    			lens += 1
    		else:
    			max_len = lens if lens > max_len else max_len
    			lens = i - flag[ord(s[i])]   			
    			for j in memory[:memory.index(ord(s[i]))+1]:
    				flag[j] = -1
    				memory.remove(j)
    			memory.append(ord(s[i]))
    		flag[ord(s[i])] = i    		
    	max_len = lens if lens > max_len else max_len
    	return max_len



s = Solution()
print(s.lengthOfLongestSubstring("abab"))