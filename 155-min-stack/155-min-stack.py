class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack_min = []
       

    def push(self, val: int) -> None:
        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)
        self.stack1.append(val)

    def pop(self) -> None:
        curr = self.stack1.pop()
        if curr == self.stack_min[-1]:
            self.stack_min.pop()
            
    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()