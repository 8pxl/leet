import time
from lib import *

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[int]  = []
        ans: list[int] = []
        for i in range (len(temperatures)-1, -1, -1):
            print(temperatures[i])
            print([temperatures[i] for i in stack])
            if not stack:
                stack.append(i)
                ans.append(0)
                continue

            x = stack.pop()
            while temperatures[i] >= temperatures[x]:
                if not stack:
                    ans.append(0)
                    stack.append(i)
                    break
                x = stack.pop()
            else:
                ans.append(x-i)
                stack.append(x)
                stack.append(i)
        return ans[::-1]


test = Solution()
curr = time.time()
sol = test.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]

)
print("finished in ", time.time() - curr)
print(sol)
