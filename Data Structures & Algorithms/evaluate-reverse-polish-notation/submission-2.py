from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() +  stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                x,y = stack.pop(), stack.pop()
                stack.append(y-x)
            elif c == "/":
                x,y = stack.pop(),stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(c))
        return stack[0]

        