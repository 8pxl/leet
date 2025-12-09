import time
from lib import *

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        turt = nums[0]
        hare = nums[nums[0]]
        while turt != hare:
            turt = nums[turt]
            hare = nums[nums[hare]]
        hare = 0
        while hare != turt:
            turt = nums[turt]
            hare = nums[hare]
        return turt


test = Solution()
curr = time.time()
sol = test.findDuplicate([2,5,9,6,9,3,8,9,7,1]

)
print("finished in ", time.time() - curr)
print(sol)

"""
whats a property unique to the place where it cycles

0 1 2 3 4 5 6 7 8 9 
2 5 9 6 9 3 8 9 7 1
  *   *   * * * * *

the fact that we reached the cycle means that there are two ways to get into the cycle
meaning that theres a duplicate. 
first, form "outside" we were able to reach a node 
and then second, from "inside" we are able to reach the same node

now how are we able to find this common node ?

what can we say about
bro this provlem 
"""
