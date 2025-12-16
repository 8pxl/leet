import time
from lib import *

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        arr = nums
        while lo <= hi:
            mid = (lo + hi) >> 1
            val= arr[mid]
            if val < target:
                lo = mid + 1
            elif val > target:
                hi = mid - 1
            else:
                return mid
        return -1



test = Solution()
curr = time.time()
sol = test.search([-1,0,3,5,9,12], 3)
print("finished in ", time.time() - curr)
print(sol)
