
class Solution:
	def judge(self, s: str, maxPal: str, i: int, j: int) -> str:
		while i >= 0 and j < len(s) and s[i] == s[j]:
			i -= 1
			j += 1
		if len(maxPal) < j - i - 1:
			maxPal = s[i + 1 : j]
		return maxPal

	def longestPalindrome(self, s: str) -> str:
		if len(s) == 0 or len(s) == 1:
			return s
		maxPal = ""
		for k in range(1, len(s)):
			maxPal = self.judge(s, maxPal, k - 1, k + 1)
			if s[k] == s[k-1]:
				maxPal = self.judge(s, maxPal, k - 1, k)
		return maxPal


