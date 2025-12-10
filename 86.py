import time
from lib import *

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0, None)
        newHead = dummy
        curr = head
        tail = ListNode(0, None)
        tailHead = tail
        while curr:
            next = curr.next
            curr.next = None
            if curr.val < x:
                dummy.next = curr
                dummy = dummy.next
            else:
                tail.next = curr
                tail = tail.next

            curr = next
        dummy = newHead.next
        while dummy and dummy.next:
            dummy = dummy.next
        if dummy:
            dummy.next = tailHead.next
        else: newHead.next = tailHead.next
        return newHead.next


test = Solution()
curr = time.time()
sol = test.partition(arrtoll([1]
), 0)
print("finished in ", time.time() - curr)
sol.print()
