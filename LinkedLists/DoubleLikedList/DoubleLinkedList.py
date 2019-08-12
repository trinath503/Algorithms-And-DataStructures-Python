class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    head = None
    tail = None

    def show(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def PushFront(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def PopFront(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next


    def PushBack(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    def PopBack(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                current_node = self.head
                while current_node.next.next is not None:
                    current_node = current_node.next

                current_node.next = None
                self.tail = current_node

    def addAfter(self,ele, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == ele:
                node =Node(data)
                if current_node ==self.head:
                    node.prev = current_node
                    if current_node.next is not None:
                        current_node.next.prev =  node
                    current_node.next = node
                elif current_node ==self.tail:
                    current_node.next = node
                    node.prev = current_node
                    self.tail = node
                else:
                    node.prev = current_node
                    node.next = current_node.next
                    current_node.next.prev = node
                    current_node.next = node
            current_node = current_node.next




tri = DoubleLinkedList()
tri.PushFront(1)
# tri.show()
tri.PushFront(2)
# tri.show()
tri.addAfter(1,10)
# tri.PopFront()
tri.PushBack(3)

tri.show()
