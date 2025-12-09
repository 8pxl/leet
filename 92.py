import time
from lib import *

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> Node:
        stack: list[ListNode] = []
        curr = head
        index = 1
        while index <= right:
            assert(curr is not None)
            if left <= index <= right:
                stack.append(curr)
            index += 1
            curr = curr.next
        end = curr
        start = ListNode(0, head)
        curr = start
        index = 0
        while index+1 < left:
            curr = curr.next
            index += 1
        while len(stack) > 0:
            curr = curr.next
            node = stack.pop()
            print(node)
            curr.next = node
        curr.next = end
        return start.next


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
