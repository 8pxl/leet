import time
from lib import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Node:
        def getNumber(l: ListNode) -> int:
            curr = l
            num = 0
            pow = 0
            while curr:
                num += curr.val * (10**pow)
                curr = curr.next
                pow += 1
            return num

        sum = str(getNumber(l1) + getNumber(l2))[::-1]
        curr = ListNode(0)
        head = curr
        for char in sum:
            curr.next = ListNode(int(char))
            curr = curr.next
        return head.next


test = Solution()
curr = time.time()
sol = test.addTwoNumbers(arrtoll([2,4,3]), arrtoll([5,6,4]))
print("finished in ", time.time() - curr)
sol.print()
