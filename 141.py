import time
from lib import *

class Solution:
    def hasCycle(self, head: Node) -> bool:
        if not head:
            return False
        seen: set[ListNode] = set()
        curr = head
        while curr:
            print(curr)
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False


test = Solution()
curr = time.time()
sol = test.hasCycle(arrtoll([3,2,0,-4]))
print("finished in ", time.time() - curr)
print(sol)
