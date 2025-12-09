import time
from lib import *

class Solution:
    def detectCycle(self, head: ListNode) -> Node:
        if (not head) or (not head.next): return None
        turt = hare = head
        while hare and hare.next:
            turt = turt.next
            hare = hare.next.next
            if turt is hare: break
        else:
            return None
        hare = head
        while turt != hare:
            turt = turt.next
            hare = hare.next
        return turt
      


test = Solution()
curr = time.time()
sol = test.detectCycle(arrtoll([3,2,0,-4]))
print("finished in ", time.time() - curr)
print(sol)
