import time
from lib import *

class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = mid = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            check = nums[mid]
            if check > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        return nums[lo]



test = Solution()
curr = time.time()
sol = test.findMin([4,5,6,7,8,1,2,3])
print("finished in ", time.time() - curr)
print(sol)
