class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                #int()结果向零取整，即正数向下取整、负数向上取整，注意与//的区别，小心有坑
                stack.append(int(num2 / num1))
            else:
                stack.append(int(c))
                
        return stack[0]