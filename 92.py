import time
from lib import *

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> Node:
        stack: list[ListNode] = []
        mid = left + ((left-right) // 2)
        index = 1
        curr = head
        while curr:
            next = curr.next
            if index <=mid:
                stack.append(curr)
            else:
                node = stack.pop()
                temp = node
                node.next = curr
                curr.next = temp.next
            curr = next
            index += 1


test = Solution()
curr = time.time()
sol = test.reverseBetween(arrtoll([1,2,3,4,5]), 2,4)
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
