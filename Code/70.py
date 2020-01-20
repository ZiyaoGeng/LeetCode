
class Solution:
	"""
    def climbStairs(self, n: int) -> int:
    	if n == 1:
    		return 1
    	if n == 2:
    		return 2
    	count = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    	return count
    """

	def climbStairs(self, n: int) -> int:
		if n == 1:
			return 1
		if n == 2:
			return 2
		stairs = [1, 2]
		for i in range(2, n):
			stairs.append(stairs[i-1] + stairs[i-2])
		return stairs[n-1]

s = Solution()
print(s.climbStairs(6))