from math import floor
import time
from lib import *

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "/", "-", "*"}
        stack: list[int] = []
        for char in tokens:
            print(stack)
            if char in operators:
                y =  stack.pop()
                x = stack.pop()
                match char:
                    case "+":
                        stack.append(x+y)
                    case "/":
                        stack.append(int(x/y))
                    case "-":
                        stack.append(x-y)
                    case "*":
                        stack.append(x*y)
            else:
                stack.append(int(char))
        return stack.pop()


test = Solution()
curr = time.time()
sol = test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print("finished in ", time.time() - curr)
print(sol)
