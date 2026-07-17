from collections import deque
class Solution:

    def ops(self, op, a, b):
        if op=="+":
            return a+b
        elif op=="-":
            return a-b
        elif op=="/":
            return int(a/b)
        else:
            return a*b

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = deque()
        for token in tokens:
            if not token.isalnum() and len(token)==1:
                value = self.ops(token, stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[-1]

        