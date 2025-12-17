from math import inf
import time
from lib import *

class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.minimums: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.getMin():
            self.minimums.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.getMin():
            self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]
        else:
            return inf


test = MinStack()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
