"""
Pyright: Cannot assign to attribute "next" for class "Node"
  Expression of type "Node" cannot be assigned to attribute "next" of class "Node"
    "Node" is not assignable to "None" [reportAttributeAccessIssue]

using this will remove this.. it does not throw runtime error
self.next: Node | None = None

self.next: Node | None -> type annotation
"= None" -> assignment / initialization
next will either be Node or None type
but for now assign it with None
The annotation does not enforce anything at runtime. You could still do:
next = 30 at runtime, pyright is displaying error

if i just do self.next: Node | None -> this part is just for editor/pyright typechecking
and it does not create any variable.. remember theres no initialization only assignment
so later when i do head.next -> throws an error -->
AttributeError: 'Node' object has no attribute 'next'

"""


class Node:
    def __init__(self, data):
        self.date = data
        self.next: Node | None = None


def print_list(head: Node | None):
    if head is None:
        print("list is empty")

    tmp = head
    while tmp is not None:
        print(tmp.date, end=" ")
        tmp = tmp.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print_list(head)
