class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        #确保栈不为空
        if self.empty():
            return None
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
                
        return self.output_stack.pop()

    def peek(self) -> int:
        #确保栈不为空
        res = self.pop()
        self.output_stack.append(res)
        return self.output_stack[-1]

    def empty(self) -> bool:
        
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()