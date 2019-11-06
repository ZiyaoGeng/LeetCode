
"""
最长回文子串
解题思路:
考虑两种回文子串的情况
"""
class Solution:
	def judge(self, j, k, s, max_start, max_end):
		while j >= 0 and k < len(s) and s[j] == s[k]:
    			j -= 1
    			k += 1
		if k - j - 1 > max_end - max_start:
			max_start = j + 1
			max_end = k
		return max_start, max_end

	def longestPalindrome(self, s: str) -> str:
		lens = len(s)
		max_start, max_end = 0, 1
		for i in range(lens):
			j, k = i, i + 1
			max_start, max_end = self.judge(j, k, s, max_start, max_end)
			j, k = i - 1, i + 1
			max_start, max_end = self.judge(j, k, s, max_start, max_end)
		return s[max_start:max_end]

s = Solution()
print(s.longestPalindrome('cbbd'))

