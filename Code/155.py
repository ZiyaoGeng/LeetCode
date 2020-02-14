
class MinStack:

    def __init__(self):
        self.stack = [0] * 10000
        self.minlist = [0] * 10000
        self.topIndex = -1
        

    def push(self, x: int) -> None:
    	self.topIndex += 1
    	self.stack[self.topIndex] = x
    	if self.topIndex == 0 or self.minlist[self.topIndex-1] > x:
    		self.minlist[self.topIndex] = x
    	else:
    		self.minlist[self.topIndex] = self.minlist[self.topIndex - 1]
    	


    def pop(self) -> None:
    	self.topIndex -= 1

    def top(self) -> int:
    	return self.stack[self.topIndex]

    def getMin(self) -> int:
    	if self.topIndex == -1:
    		return None
    	return self.minlist[self.topIndex]
