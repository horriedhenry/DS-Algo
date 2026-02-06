class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


# Stack : insert, delete from front
class Stack:
    def __init__(self):
        self.head: Node | None = None
        self.length = 0

    def push(self, data: int):
        # dont need to check if head is None; if it is None the new_node.next will be None
        # which will be first node in the stack
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        self.length += 1

    def pop(self) -> int | None:
        if self.head is None:
            return None

        head = self.head
        self.head = self.head.next

        self.length -= 1

        return head.data

    def peek(self) -> int | None:
        if self.head is None:
            return None

        return self.head.data
