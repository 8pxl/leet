import time
from lib import *

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(head.val-1, head)
        curr = dummy.next
        prev = dummy
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


test = Solution()
curr = time.time()
sol = test.deleteDuplicates(arrtoll([1,1,1,1,1,1]))
print("finished in ", time.time() - curr)
sol.print()
