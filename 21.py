import time
from lib import *

class Solution:
    def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
        if not list1: return list2
        if not list2: return list1
        if list1.val <=list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

test = Solution()
curr = time.time()
sol = test.mergeTwoLists(arrtoll([1,2,4]), arrtoll([1,3,4]))
print("finished in ", time.time() - curr)
_ = sol and sol.print()
# print(sol)
