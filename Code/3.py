
"""
无重复字符的最长子串
解题思路:
1、设置一个标记列表，判断当前有哪些字符算在目前的长度中。
2、设置一个记忆列表，记录当前有哪些字符（主要是顺序）
3、若当前字符不存在，记忆数组则记录当前字符，长度+1；若存在，取最大长度，并
计算当前不重复字符长度，并删除记忆数组中在重复字符之前的字符。
结果:
执行用时 :80 ms, 在所有 python3 提交中击败了75.47%的用户
内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.01%的用户
反思:
两个列表可以变成一个。
"""
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