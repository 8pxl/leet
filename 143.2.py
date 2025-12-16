import time
from lib import *

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # redo by reversing the second half and then merging the two lists
        pass


test = Solution()
curr = time.time()
sol = test.reorderList(arrtoll([1]

))
print("finished in ", time.time() - curr)
print(sol)

"""
0,1,2,3,4 ... n-1, n

0, n  1, n-1, 2, n-2, 3, n-3, 4, n-4, 5, n-5, 6

the list ends at (something close to) n/2
"""
