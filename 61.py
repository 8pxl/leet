import time
from lib import *

class Solution:
    def rotateRight(self, head: Node, k: int) -> Node:
        if not head or (k == 0):
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        dummy = ListNode(0, head)
        curr.next = dummy.next
        k = k % length
        newTail = length - k - 1
        index = 0
        curr = dummy.next
        while index < newTail:
            curr = curr.next
            index += 1
        newHead = curr.next
        curr.next = None
        dummy.next = newHead
        return dummy.next


test = Solution()
curr = time.time()
sol = test.rotateRight(arrtoll([1,2,3,4,5]), 5)
print("finished in ", time.time() - curr)
sol.print()
# print(sol)


"""
1 2 3 4 5
4 5 1 2 3


5 -> 1
3 -> none
z -> 4
"""
