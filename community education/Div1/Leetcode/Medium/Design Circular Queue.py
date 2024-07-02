class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.l = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail
        self.tail.next = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.l += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.l -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k