import time
from lib import *

class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }
        stack: list[str] = []
        for char in s:
            if char in closing:
                stack.append(closing[char])
            elif stack and (char == stack[-1]):
                stack.pop()
            else:
                return False
        return len(stack) == 0

test = Solution()
curr = time.time()
sol = test.isValid("]]]]")
print("finished in ", time.time() - curr)
print(sol)
