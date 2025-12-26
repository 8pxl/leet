import time
from lib import *

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo = mid = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if nums[mid] > target:
                hi = mid-1
            elif nums[mid] <= target:
                lo = mid+1
        if not nums or (nums[lo-1] != target):
            return [-1,-1]
        ub = lo-1
        lo = mid = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if nums[mid] >= target:
                hi = mid-1
            elif nums[mid] < target:
                lo = mid+1
        return ([lo, ub])

test = Solution()
curr = time.time()
sol = test.searchRange([0], 8)
print("finished in ", time.time() - curr)
print(sol)
