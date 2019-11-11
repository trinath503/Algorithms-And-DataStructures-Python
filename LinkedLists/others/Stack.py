class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev =prev
        self.data =data
        self.next = next



class Stack:
    head = None
    tail = None

    def Push(self,data):
        node = Node(data)
        if self.head is not None:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def Pop(self):
        if self.tail is not Node:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def show(self):
        current_data = self.head
        while current_data is not None:
            print(current_data.data)
            current_data = current_data.next





tri = Stack()
tri.Push(1)
tri.Push(3)

tri.Push(5)
tri.Pop()
tri.Push(2)
tri.show()