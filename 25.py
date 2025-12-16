import time
from lib import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head.next:
            return head
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1

        dummy = ListNode(-1,head)
        start = dummy
        curr = head
        new_start = curr
        next = curr.next
        for _ in range(count // k):
            print(curr)
            new_start = curr
            print("new_start:", new_start)
            prev = dummy
            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            print(prev)
            start.next = prev
            start = new_start
        new_start.next = next
        return dummy.next


test = Solution()
curr = time.time()
sol = test.reverseKGroup(arrtoll([1]), 1)
print("finished in ", time.time() - curr)
sol.print()
