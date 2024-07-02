class MinStack(object):

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val):
        self.stack.append(val)
        val = min(val,self.m[-1] if self.m else val)
        self.m.append(val)
        

    def pop(self):
        self.stack.pop() 
        self.m.pop() 
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()