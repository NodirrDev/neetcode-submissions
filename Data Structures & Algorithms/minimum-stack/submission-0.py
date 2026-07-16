from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mins = deque()
        

    def push(self, val: int) -> None:
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        self.stack.append(val)
        
        

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.mins[-1]:
            self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]

        
