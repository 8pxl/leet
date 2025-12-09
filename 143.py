import time
from lib import *

class Solution:
    def reorderList(self, head: ListNode) -> None:
        stack: list[ListNode] = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head
        stack = stack[(len(stack)+1)//2:]
        print(stack)
        print("-----------")
        temp = curr.next
        while len(stack) > 0:
            temp = curr.next
            curr.next = stack.pop()
            if temp is curr.next:
                curr.next.next = None
            else:
                curr.next.next = temp
                curr = temp
        if curr.next:
            if curr.next.next:
                curr.next.next.next = None
        # curr.next = None
        # head.print()


test = Solution()
curr = time.time()
sol = test.reorderList(arrtoll([1]

))
print("finished in ", time.time() - curr)
print(sol)

"""
0,1,2,3,4 ... n-1, n

0, n  1, n-1, 2, n-2, 3, n-3, 4, n-4, 5, n-5, 6

the list ends at (something close to) n/2
"""
