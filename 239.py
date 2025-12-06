import time
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        sol: list[int] = []
        mdq: deque[int] = deque()
        for right in range(len(nums)):
            left = right+1 - k
            while len(mdq) > 0 and (nums[right] > nums[mdq[-1]]):
                _ = mdq.pop()
            mdq.append(right)
            if right < k-1:
                continue
            sol.append(nums[mdq[0]])
            if mdq[0] == left:
                _ = mdq.popleft()
        return sol


test = Solution()
curr = time.time()
sol = test.maxSlidingWindow([1,3,1,2,0,5], 3)
print("finished in ", time.time() - curr)
print(sol)


"""
1000, 900, 3,3,3,300,3,3,3,
"""
