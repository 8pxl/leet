import time
from lib import *

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        lo = mid = 0
        hi = len(nums) - 1
        while lo < hi-1:
            mid = (lo + hi) >> 1
            ln = nums[mid-1]
            rn = nums[mid+1]
            if nums[mid] > ln and nums[mid] >= rn:
                return mid
            elif nums[mid] <= rn:
                lo = mid+1
            else:
                hi = mid-1
        if nums[hi] > nums[lo]:
            return hi
        return lo
 
test = Solution()
curr = time.time()
sol = test.findPeakElement([2, 1])
print("finished in ", time.time() - curr)
print(sol)
