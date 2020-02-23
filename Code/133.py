import sys
sys.path.append('../functions/')
from Graph import Node

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
    	if node == None:
    		return []
    	visited = [[0] * 101 for i in range(101)]
    	cloneNode = Node(node.val, [])
    	def dfs(node, cloneNode):
    		for n in node.neighbors:
    			if visited[node.val][n.val] == 0:
    				new = Node(n.val, [cloneNode])
    				visited[node.val][n.val] = 1
    				visited[n.val][node.val] = 1
    				cloneNode.neighbors.append(new)
    				dfs(n, new)
    	dfs(node, cloneNode)
    	return cloneNode

"""
class Solution(object):

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return node
        if node in self.visited:
        	return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node
"""