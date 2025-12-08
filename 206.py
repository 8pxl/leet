import time
from lib import *

class Solution:
    def reverseList(self, head: ListNode) -> Node:
        prev: Node = None
        curr: Node = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def recurseRev(self, curr: Node) -> Node:
        if not curr:
            return None
        new = curr
        if curr.next:
            new = self.recurseRev(curr.next)
            curr.next.next = curr
        curr.next = None
        return new



test = Solution()
curr = time.time()
sol = test.recurseRev(arrtoll([1,2,3,4,5]))
print("finished in ", time.time() - curr)
_ = sol and sol.print()
