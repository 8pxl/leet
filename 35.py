import time
from lib import *

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, mid = 0, 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return lo


test = Solution()
curr = time.time()
sol = test.searchInsert([1,3,5,6], 4)
print("finished in ", time.time() - curr)
print(sol)
