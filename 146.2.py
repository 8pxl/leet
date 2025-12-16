import time
from typing import override

class ListNode:
    def __init__(self, val: int = -1, next: ListNode | None = None, prev : ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next
        self.prev: ListNode | None = prev
    @override
    def __str__(self):
        return str(self.val)
    def print(self):
        print(self.val)
        if self.next:
            self.next.print()

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.map: dict[int, int] = {}
        self.llmap: dict[int, ListNode] = {}
        self.head: ListNode = ListNode()
        self.tail: ListNode = ListNode()

    def append(self, node: ListNode):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def drop_head(self):
        old_head= self.head.next
        new_head= old_head.next
        new_head.prev = self.head
        if new_head.next:
            new_head.next.prev = new_head
        self.head.next = new_head

        del self.map[old_head.val]
        del self.llmap[old_head.val]

    def update(self, key:int):
        node = self.llmap[key]
        #break links
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.append(node)
        else:
            assert node is self.tail
        node.next = None

    def get(self, key: int) -> int:
        print("get: ", key)
        # self.head.print()
        if key in self.map:
            self.update(key)
        return self.map.get(key, -1)

    def put(self, key: int, value: int) -> None:
        print("put: ", key, value)
        # self.head.print()
        if (key not in self.map):
            newNode = ListNode(key, None)
            if not self.head.next:
                print("no head found, setting new head")
                self.head.next = newNode
                newNode.prev = self.head
                self.tail = newNode
            else:
                self.append(newNode)
                if (len(self.map) >= self.capacity):
                    assert(self.head.next)
                    self.drop_head()
            self.llmap[key] = newNode
        else:
            self.update(key)
        self.map[key] = value
        print(self.map)


# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(1)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.put(3, 3)
lRUCache.put(4, 4)
print(lRUCache.get(4))
print(lRUCache.get(3))
print(lRUCache.get(2))
print(lRUCache.get(1))
lRUCache.put(5, 5)
print(lRUCache.get(1))
print(lRUCache.get(2))
print(lRUCache.get(3))
print(lRUCache.get(4))
print(lRUCache.get(5))
