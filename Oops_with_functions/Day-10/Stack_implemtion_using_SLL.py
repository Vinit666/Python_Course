class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, node=None) -> None:
        self.head = node

    def top(self):
        if self.head == None:
            print("SLL not initialized")

        else:
            print(self.head.value)

    def push(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            print("Cannot pop")

        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None

    def display(self):
        if self.head == None:
            print("SLL is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next


n1 = Node(100)
n2 = Node(200)
n3 = Node(300)


sll = SinglyLinkedList()
sll.push(n1)
sll.push(n2)
sll.push(n3)
sll.pop()
sll.display()
