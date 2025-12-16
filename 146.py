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

    def update(self, key:int):
        node = self.llmap[key]
        #break links
        self.head.print()
        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            print(self.tail.val, node.val)
            assert node is self.tail
        node.next = None

    def get(self, key: int) -> int:
        print("get", key)
        if key in self.map:
            self.update(key)
        print(self.map.get(key, -1))
        print("tail val: ", self.tail.val)
        return self.map.get(key, -1)

    def put(self, key: int, value: int) -> None:
        print("put", key, value)
        print("tail val: ", self.tail.val)
        if (key not in self.map):
            newNode = ListNode(key, None)
            if not self.head.next:
                newNode.prev = self.head
                self.head.next = newNode
                self.tail = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                if (len(self.map) >=self.capacity):
                    assert(self.head.next)
                    drop = self.head.next
                    temp = self.head.next.next
                    del self.map[drop.val]
                    del self.llmap[drop.val]
                    self.head.next = temp
                    if temp:
                        self.head.next.prev = self.head
            self.llmap[key] = newNode
        else:
            self.update(key)
        self.map[key] = value
        print(self.map)

        self.head.print()
        # print(self.map,self.llmap)


# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
