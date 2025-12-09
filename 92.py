import time
from lib import *

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> Node:
        dummy = ListNode(0, head)
        start = dummy
        curr = head
        for i in range(left-1):
            start = start.next  # pyright: ignore[reportOptionalMemberAccess]
            curr = curr.next  # pyright: ignore[reportOptionalMemberAccess]
        prev = None
        for i in range(right + 1 - left):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        start.next.next = curr
        start.next = prev
        return dummy.next


test = Solution()
curr = time.time()
sol = test.reverseBetween(arrtoll(
[1,2,3,4,5]
), 2,4)
print("finished in ", time.time() - curr)
_ = sol and sol.print()
"""
1 -> 2
2 -> 3
3 -> 4
4 -> 5
5 -> null

reversed:
1 -> 4
2 -> 5
3 -> 2
4 -> 3
5 -> null

"""
