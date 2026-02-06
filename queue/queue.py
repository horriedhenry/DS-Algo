class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


# Queue : insert from rear, delete from front
class Queue:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    def enqueue(self, data: int):
        new_node = Node(data)

        if self.tail is None:
            self.tail = self.head = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

        self.length += 1

    def deque(self) -> int | None:
        if self.head is None:
            # can use print("empty") but.. just useful for debugging..
            # this way just just if this method returned None or a value..
            return None

        head = self.head

        if self.head is self.tail:
            self.head = self.tail = None
            return head.data

        self.head = self.head.next

        self.length -= 1
        return head.data

    def peek(self) -> int | None:
        if self.head is None:
            return None

        return self.head.data
