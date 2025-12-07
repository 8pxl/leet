class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None =None):
        self.val: int = val
        self.next: ListNode | None = next

def build_linked_list(values: list[int]) -> ListNode:
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head
