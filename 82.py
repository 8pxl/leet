import time
from lib import *

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(head.val-1, head)
        curr = head
        prev = dummy
        while curr and curr.next:
            if (curr.next.val == curr.val):
                while curr.next and (curr.val == curr.next.val):
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next


test = Solution()
curr = time.time()
sol = test.deleteDuplicates(arrtoll([1,1,1,2,2,2,3]))
print("finished in ", time.time() - curr)
sol.print()
