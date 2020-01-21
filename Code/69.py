
class Solution:
    def mySqrt(self, x: int) -> int:
    	if x == 0:
    		return 0
    	return self.binarySearch(x, 1, x // 2 + 1)

    def binarySearch(self, x: int, l: int, r: int) -> int:
    	mid = (l + r) // 2
    	if mid ** 2 <= x and (mid + 1) ** 2 > x:
    		return mid
    	elif mid ** 2 > x:
    		return self.binarySearch(x, l, mid)
    	elif mid ** 2 < x and (mid + 1) ** 2 <= x:
    		return self.binarySearch(x, mid + 1, r)


