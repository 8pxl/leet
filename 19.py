import time
from lib import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


test = Solution()
curr = time.time()
sol = test.removeNthFromEnd(arrtoll(
[1,2,3,4,5]
), 2)
print("finished in ", time.time() - curr)
if sol:
    sol.print()
print(sol)
