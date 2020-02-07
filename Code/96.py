
class Solution:
    def numTrees(self, n):
        G = [0]*(n+1)
        G[0], G[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]

    def numTrees(self, n: int) -> int:
    	C = 1
    	for i in range(n):
    		C = C * 2 * (2 * i + 1) / (i+2)
    	return int(C)
