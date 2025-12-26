import math
import time
from lib import *

class Solution:
    def check(self, piles: list[int], k: int, h: int) -> bool:
        t = 0
        for num in piles:
            t += math.ceil(num/k)
        return t <= h
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo = mid = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo+hi) >> 1
            if self.check(piles,mid,h):
                hi = mid
            else: lo = mid+1
        return lo


test = Solution()
curr = time.time()
sol = test.minEatingSpeed([30,11,23,4,20], 6)
print("finished in ", time.time() - curr)
print(sol)
