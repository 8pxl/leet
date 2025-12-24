import time
from lib import *

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        inflection = 0
        prev = nums[0] - 1
        for i, num in enumerate(nums):
            if num < prev:
                inflection = i
                break
            prev = num
        lo, mid = 0, 0 
        hi = len(nums) - 1
        tailLen = len(nums) - inflection
        while lo <= hi:
            mid = (lo+hi) >> 1
            midTransformed = mid
            if mid < tailLen:
                midTransformed  += inflection
            else:
                midTransformed -= tailLen
            check = nums[midTransformed]
            if check < target:
                lo = mid+1
            elif check > target:
                hi = mid-1
            else:
                return midTransformed
        return -1


test = Solution()
curr = time.time()
sol = test.search([4,5,6,6,1,2], 5)
print("finished in ", time.time() - curr)
print(sol)
