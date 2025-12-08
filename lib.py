from typing import override


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next
    @override
    def __str__(self):
        return str(self.val)
    def print(self):
        print(self.val)
        if self.next:
            self.next.print()


type Node = ListNode | None

def arrtoll(values: list[int]) -> ListNode:
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head
